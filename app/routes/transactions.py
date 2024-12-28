from flask import Blueprint, request, jsonify
from app.models import Transaction, Account, Category, db

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/<int:account_id>', methods=['POST'])
def create_transaction(account_id):
    data = request.get_json()
    try:
        account = Account.query.get(account_id)
        if not account:
            return jsonify({"status": "error", "message": "Account not found"}), 404

        category = Category.query.filter_by(name=data['category']).first()
        if not category:
            return jsonify({"status": "error", "message": "Category not found"}), 404

        transaction = Transaction(
            customer_id=account.customer_id,
            account_id=account_id,
            amount=data['amount'],
            description=data['description'],
            category_id=category.id
        )
        account.balance -= transaction.amount  # Update balance
        db.session.add(transaction)
        db.session.commit()
        return jsonify({"status": "success", "data": {"id": transaction.id, "amount": transaction.amount}}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500



from flask import Blueprint

transactions_bp = Blueprint('transactions', __name__)
# Get All Transactions for an Account
@transactions_bp.route('/<int:account_id>', methods=['GET'])
def get_all_transactions(account_id):
    try:
        account = Account.query.get(account_id)
        if not account:
            return jsonify({"status": "error", "message": "Account not found"}), 404

        transactions = Transaction.query.filter_by(account_id=account_id).all()
        transactions_data = [
            {"id": transaction.id, "amount": transaction.amount, "description": transaction.description, "transaction_date": transaction.transaction_date, "category_id": transaction.category_id}
            for transaction in transactions
        ]
        return jsonify({"status": "success", "data": transactions_data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
from flask import Blueprint, request, jsonify
from app.models import Account, Customer, db

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/<int:customer_id>', methods=['POST'])
def create_account(customer_id):
    data = request.get_json()
    try:
        customer = Customer.query.get(customer_id)
        if not customer:
            return jsonify({"status": "error", "message": "Customer not found"}), 404

        account = Account(
            customer_id=customer_id,
            account_name=data['account_name'],
            account_type=data['account_type'],
            balance=data.get('balance', 0.0)
        )
        db.session.add(account)
        db.session.commit()
        return jsonify({"status": "success", "data": {"id": account.id, "balance": account.balance}}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# Get All Accounts for a Customer
@accounts_bp.route('/<int:customer_id>', methods=['GET'])
def get_all_accounts(customer_id):
    try:
        customer = Customer.query.get(customer_id)
        if not customer:
            return jsonify({"status": "error", "message": "Customer not found"}), 404

        accounts = Account.query.filter_by(customer_id=customer_id).all()
        accounts_data = [
            {"id": account.id, "account_name": account.account_name, "account_type": account.account_type, "balance": account.balance}
            for account in accounts
        ]
        return jsonify({"status": "success", "data": accounts_data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
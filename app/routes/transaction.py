from flask import Blueprint, request, jsonify

# Create a Blueprint for transactions
transaction_bp = Blueprint('transaction', __name__)

# Sample data to simulate a database
transactions = [
    {"id": 1, "customer_id": 1, "amount": 100.50, "currency": "USD", "tag": "Groceries", "date": "2024-12-01"},
    {"id": 2, "customer_id": 2, "amount": 50.00, "currency": "USD", "tag": "Entertainment", "date": "2024-12-02"}
]

# Route to get all transactions
@transaction_bp.route('/transactions', methods=['GET'])
def get_transactions():
    return jsonify({"transactions": transactions})

# Route to get a transaction by ID
@transaction_bp.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    transaction = next((t for t in transactions if t['id'] == transaction_id), None)
    if transaction:
        return jsonify(transaction)
    else:
        return jsonify({"error": "Transaction not found"}), 404

# Route to create a new transaction
@transaction_bp.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    if not data or not all(k in data for k in ("customer_id", "amount", "currency", "tag", "date")):
        return jsonify({"error": "Invalid data"}), 400
    
    new_transaction = {
        "id": len(transactions) + 1,  # Simple auto-increment
        "customer_id": data['customer_id'],
        "amount": data['amount'],
        "currency": data['currency'],
        "tag": data['tag'],
        "date": data['date']
    }
    transactions.append(new_transaction)
    return jsonify(new_transaction), 201

# Route to update a transaction
@transaction_bp.route('/transactions/<int:transaction_id>', methods=['PUT'])
def update_transaction(transaction_id):
    transaction = next((t for t in transactions if t['id'] == transaction_id), None)
    if not transaction:
        return jsonify({"error": "Transaction not found"}), 404
    
    data = request.get_json()
    transaction.update({k: data[k] for k in data if k in transaction})
    return jsonify(transaction)

# Route to delete a transaction
@transaction_bp.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    global transactions
    transaction = next((t for t in transactions if t['id'] == transaction_id), None)
    if not transaction:
        return jsonify({"error": "Transaction not found"}), 404
    
    transactions = [t for t in transactions if t['id'] != transaction_id]
    return jsonify({"message": "Transaction deleted"})

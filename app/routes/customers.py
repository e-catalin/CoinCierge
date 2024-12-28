from flask import Blueprint, jsonify, request
from app.models import Customer, db

customers_bp = Blueprint('customers', __name__)

@customers_bp.route('/', methods=['GET'])
def get_all_customers():
    """
    Fetch all customers from the database.
    """
    try:
        customers = Customer.query.all()
        customers_data = [
            {"id": customer.id, "name": customer.name, "email": customer.email}
            for customer in customers
        ]
        return jsonify({"status": "success", "data": customers_data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@customers_bp.route('/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    """
    Fetch a specific customer by ID.
    """
    try:
        customer = Customer.query.get(customer_id)
        if not customer:
            return jsonify({"status": "error", "message": "Customer not found"}), 404

        customer_data = {"id": customer.id, "name": customer.name, "email": customer.email}
        return jsonify({"status": "success", "data": customer_data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@customers_bp.route('/', methods=['POST'])
def create_customer():
    data = request.get_json()
    try:
        customer = Customer(
            name=data['name'],
            email=data['email'],
            password=data['password']
        )
        db.session.add(customer)
        db.session.commit()
        return jsonify({"status": "success", "data": {"id": customer.id, "name": customer.name}}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500



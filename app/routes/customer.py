from flask import Blueprint, jsonify, request
from app.models import Customer, db

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{"id": c.id, "name": c.name, "email": c.email} for c in customers])

@customer_bp.route('/', methods=['POST'])
def create_customer():
    data = request.json
    customer = Customer(name=data['name'], email=data['email'], password=data['password'])
    db.session.add(customer)
    db.session.commit()
    return jsonify({"id": customer.id, "name": customer.name, "email": customer.email}), 201

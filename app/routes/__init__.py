def register_routes(app):
    from .customer import customer_bp
    from .transaction import transaction_bp

    app.register_blueprint(customer_bp, url_prefix='/api/customers')
    app.register_blueprint(transaction_bp, url_prefix='/api/transactions')

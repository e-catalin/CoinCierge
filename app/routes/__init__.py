def register_routes(app):
    from app.routes.transaction import transaction_bp
    from app.routes.customer import customer_bp

    app.register_blueprint(customer_bp, url_prefix='/customers')
    app.register_blueprint(transaction_bp, url_prefix='/transactions')

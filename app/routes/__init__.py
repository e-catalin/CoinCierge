def register_routes(app):
    from app.routes.customers import customers_bp
    from app.routes.accounts import accounts_bp
    from app.routes.transactions import transactions_bp


    app.register_blueprint(customers_bp, url_prefix='/customers')
    app.register_blueprint(transactions_bp, url_prefix='/transactions')
    app.register_blueprint(accounts_bp, url_prefix='/accounts')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
from app.config import Config

# Initialize Flask extensions
db = SQLAlchemy()  # Initialize SQLAlchemy instance
migrate = Migrate()

def create_app():
    """Factory function to create a Flask application instance."""
    # Load environment variables from .env file
    load_dotenv()

    # Create Flask app
    app = Flask(__name__)

    # Get database URI from Config (this will trigger the password prompt if necessary)
    db_uri = Config.get_database_uri()  # This ensures we prompt for the password once

    # Set up database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

    # Initialize Flask extensions with the app
    db.init_app(app)  # This line links the Flask app to the SQLAlchemy instance
    migrate.init_app(app, db)
    CORS(app)

    # Attempt to connect to the database once at the start
    try:
        with app.app_context():
            db.engine.connect()  # Test database connection
    except Exception as e:
        app.logger.error(f"Database connection failed: {e}")
        raise Exception("Failed to connect to the database. Please check your credentials and try again.")

    # Import and register blueprints
    from app.routes import register_routes
    register_routes(app)

    @app.route('/')
    def home():
        return 'Hello World!'

    @app.route('/sum/<x>/<y>')
    def test(x: int, y: int):
        print('This is a test')
        sum = int(x) + int(y)
        return {'x': x, 'y': y, 'Sum': sum}

    return app

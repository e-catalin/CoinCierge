from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
import os
from getpass import getpass

# Initialize Flask extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """Factory function to create a Flask application instance."""
    # Load environment variables from .env file
    load_dotenv()

    # Create Flask app
    app = Flask(__name__)

    # Prompt for the database password
    db_password = getpass("Enter database password: ")

    # Set up database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql://{os.getenv('DB_USER')}:{db_password}@"
        f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Import and register blueprints
    with app.app_context():
        from app.routes import register_routes
        register_routes(app)

    @app.route('/')
    def home():
        return 'Hello, World!'

    return app

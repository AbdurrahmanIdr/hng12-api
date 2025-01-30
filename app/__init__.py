from flask import Flask
from flask_cors import CORS


def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)

    # Enable CORS (allows cross-origin requests)
    CORS(app)

    # Register Blueprints or Routes
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app

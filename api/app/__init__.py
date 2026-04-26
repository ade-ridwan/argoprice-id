from flask import Flask
from .utils.exceptions import register_error_handlers # Import handler
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init Extensions
    db.init_app(app)
    ma.init_app(app)
    register_error_handlers(app)


    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Register Blueprints
    from app.routes.auth_routes import auth_bp # Import auth
    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    
    return app

from flask import Flask
from flask_login import LoginManager
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login = LoginManager()
    
login.login_view = 'user_bp.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions here (e.g., SQLAlchemy, Migrate)
    db.init_app(app)
    login.init_app(app)
    
    # Register blueprints here
    from app.routes import user_route, contact_route, error_route
    app.register_blueprint(user_route.user_bp)
    app.register_blueprint(contact_route.contact_bp)

    # Error handlers blueprint (registering functions)
    app.register_blueprint(error_route.errors_bp)
    return app
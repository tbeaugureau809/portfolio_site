from flask import Flask
from app.routes.core_routes import bp as core_bp
from app.routes.navigation import bp as navigation_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(core_bp)
    app.register_blueprint(navigation_bp)

    return app
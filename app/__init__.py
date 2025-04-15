from flask import Flask
from app.Config import Config
from app.routes import sales_bp
from app.extension import db

def create_application():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    # Blueprint Intialize
    app.register_blueprint(sales_bp, url_prefix='/api/sales')
    return app

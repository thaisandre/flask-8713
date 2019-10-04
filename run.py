from flask import Flask
from my_app.views import conta_bp
from my_api import api_bp
from database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.template_folder = 'my_app/templates'
    app.static_folder = 'my_app/static'
    app.register_blueprint(conta_bp)
    app.register_blueprint(api_bp)
    db.init_app(app)
    return app

def setup_db(app):
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app = create_app()
    setup_db(app)
    app.run()
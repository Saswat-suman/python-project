from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db

#app = Flask(__name__)
#app.config.from_object(Config)

#db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .errors import errors as errors_blueprint
    app.register_blueprint(errors_blueprint)

    return app
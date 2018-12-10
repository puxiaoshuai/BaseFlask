from flask import Flask
import config
from exts import db
from flask_migrate import Migrate
from flask_login import LoginManager
from apps.admin import admin
from apps.front import front


def regigter_blueprints(app):
    app.register_blueprint(admin)
    app.register_blueprint(front)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.configs.get(config_name))
    db.init_app(app)
    Migrate(db=db, app=app)
    regigter_blueprints(app)
    return app


if __name__ == '__main__':
    app = create_app("development")
    app.run(port=1210, debug=True)

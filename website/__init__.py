from flask import *


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    from .routes import main
    app.register_blueprint(main)

    return app

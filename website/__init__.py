from flask import *


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    from website.main.routes import main
    from website.technical_projects.routes import technical_project
    from website.poems.routes import poem_bp
    from website.materials.routes import materials_bp

    app.register_blueprint(main)
    app.register_blueprint(technical_project)
    app.register_blueprint(poem_bp)
    app.register_blueprint(materials_bp)

    return app

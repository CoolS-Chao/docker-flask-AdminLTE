from flask import Flask
from src.backend_api.main_service.blogs.controller import bg


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bg)

    return app


if __name__ == "__main__":
    create_app().run()
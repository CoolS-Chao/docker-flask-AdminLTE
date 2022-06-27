from flask import Flask
from src.backend_api.users.controller import ul


def create_app():
    app = Flask(
        __name__,
        template_folder="src/templates",
        static_folder="src/static",
    )
    app.register_blueprint(ul)

    return app


if __name__ == "__main__":
    create_app().run()
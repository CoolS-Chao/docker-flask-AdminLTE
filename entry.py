from flask import Flask
from src.backend_api.users.controller import ul


def create_app():
    app = Flask(
        __name__,
        template_folder="src/templates",
        static_folder="src/static",
    )
    app.register_blueprint(ul)
    app.config.from_object("config.prodConfig.ProductionConfig")

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)
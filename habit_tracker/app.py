from flask import Flask
import connexion


def create_app() -> Flask:
    app = connexion.FlaskApp(__name__, specification_dir='../openapi/')
    app.add_api('habit.openapi.yaml')
    return app.app

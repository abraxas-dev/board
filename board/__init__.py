import os
from dotenv import load_dotenv
from flask import Flask
from board import pages
from board import database
from board import auth

load_dotenv()

def create_app():

    app = Flask(__name__)
    app.config.from_prefixed_env()
    app.register_blueprint(pages.bp)
    app.register_blueprint(auth.bp)
    database.init_app(app)

    return app

if __name__ == '__init__':
    create_app()
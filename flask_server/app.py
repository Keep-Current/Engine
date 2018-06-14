from flask import Flask

from flask_server.rest import extract_keywords, compare_doc
from flask_server.settings import DevConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(extract_keywords.blueprint)
    app.register_blueprint(compare_doc.blueprint)
    return app
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    #initializing the application
    app = Flask(__name__)

    # setting up the configurations
    app.config.from_object(config_options[config_name])
    # app.config.from_pyfile('config.py')
    from .request import configure_request
    configure_request(app)
    bootstrap.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)



    return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from . import db


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'INTERNETPROGRAMMINGISFUN'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    

    from . import db
    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import bp as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .item import itemBp as item_blueprint
    app.register_blueprint(item_blueprint)

    # from . import models
    # with app.app_context():
    #     db.create_all()

    return app
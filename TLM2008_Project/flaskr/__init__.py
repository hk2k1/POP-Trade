import os
print("Hello i am in __init__.py beginning")
from flask import Flask, render_template
from . import db
from . import auth
from . import auction #import module

def create_app(test_config = None):
    print("Executing __init__.py...")
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY = 'InternetProgramming',
        DATABASE = os.path.join(app.instance_path,'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py',silent = True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello/<name>')
    def hello(name):
        return 'Hello, %s!'% name
    
    @app.route('/')
    def index():
        return render_template("index.html")
      
    db.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(auction.bp) #generate html to send to client

    return app
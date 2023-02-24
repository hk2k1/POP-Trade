from flask import Flask, render_template
from flaskr import db
#from . import auth

app = Flask(__name__)

#what does the @app.route() do? well, the @ symbol is a function extender for the function "app". So when app.route() is passed with "/", the function index() is called as an extension

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/auction")
def auction():
    return render_template("/auction/auctionMain.html")

@app.route("/register")
def register():
    return render_template("/auth/register.html")

@app.route("/loginpage")
def loginpage():
    return render_template("/auth/loginpage.html")

@app.route("/favourite")
def favourite():
    return render_template("/favourite.html")
#app.register_blueprint(auth.bp)

if __name__ == "__main__":
    app.run(debug=True)
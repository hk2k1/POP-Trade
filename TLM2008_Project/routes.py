from flask import Flask, render_template, Blueprint
#from . import db
#from . import auth

#main = Flask(__name__)
main = Blueprint('main',__name__)
#main.config['SQLALCHEMY_DATABASE_URI']='sqlite:///poptrade.db'
#db = SQLAlchemy(main)


# class user(db.Model):
#     uid = db.Column(db.Integer,primary_key=True)
#     content = db.Column()
#what does the @main.route() do? well, the @ symbol is a function extender for the function "main". So when main.route() is passed with "/", the function index() is called as an extension

@main.route("/")
def index():
    return render_template("index.html")

# @main.route("/auction")
# def auction():
#     return render_template("/auction/auctionMain.html") #handled by auction.py now

@main.route("/register")
def register():
    return render_template("/auth/register.html")

@main.route("/aboutus")
def aboutus():
    return render_template("/aboutus.html")

#db.init_app(main)


#main.register_blueprint(auth.bp)

if __name__ == "__main__":
    main.run(debug=True)
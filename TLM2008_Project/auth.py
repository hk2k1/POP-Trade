#this is the server code that handles routing and services for auth page

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from TLM2008_Project.db import get_db

#define blueprint to register with app upon startup
bp = Blueprint('auth', __name__, url_prefix='/auth')
print("Initializing auth.py...")

#function extension to route auth request for register resource
@bp.route('/register', methods=('GET', 'POST'))
def register():
    #if post request is received from client, process register service. Else renders register.html for client
    if request.method == 'POST':
        #retrieve username and password field from form
        username = request.form['username']
        password = request.form['password']
        #create database object to intereact with sqlite db
        db = get_db()
        error = None

        #validates field
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                #if details not used, create entry into database, else return error to client
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                #redirects client to login page
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

# #function extension to route auth request for login resource
# @bp.route('/login', methods=('GET', 'POST'))
# def login():
#     #if post request is received from client, process login service. Else renders login.html for client
#     if request.method == 'POST':
#         #retrieve username and password field from form
#         username = request.form['username']
#         password = request.form['password']
#         db = get_db()
#         error = None
#         #executes query for user, if user does not exist, return error msg to client
#         user = db.execute(
#             'SELECT * FROM user WHERE username = ?', (username,)
#         ).fetchone()

#         if user is None:
#             error = 'Incorrect username.'
#         elif not check_password_hash(user['password'], password):
#             error = 'Incorrect password.'
#         #once no error, means user is authenticated and redirects user to front page with session created for user
#         if error is None:
#             session.clear()
#             session['user_id'] = user['id']
#             return redirect(url_for('main.index'))

#         flash(error)

#     return render_template('auth/login.html')

@bp.route('/login-register',methods =('GET','POST'))
def login_register():
    if request.method == 'POST':
        state = request.form['state']
        #email = request.form['email']
        

        if state == 'login':   #if email is not send with form, client is requesting for login service
            username = request.form['username']
            password = request.form['password']
            db = get_db()
            error = None
            #executes query for user, if user does not exist, return error msg to client
            user = db.execute(
                'SELECT * FROM user WHERE username = ?', (username,)
            ).fetchone()

            if user is None:
                error = 'Incorrect username.'
            elif not check_password_hash(user['password'], password):
                error = 'Incorrect password.'
            #once no error, means user is authenticated and redirects user to front page with session created for user
            if error is None:
                session.clear()
                session['user_id'] = user['id']
                return redirect(url_for('main.index'))

            flash(error)

        elif state == 'register' :   #if email is send with form, client is requesting for registration service
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            #create database object to intereact with sqlite db
            db = get_db()
            error = None

            #validates field
            if not username:
                error = 'Username is required.'
            elif not password:
                error = 'Password is required.'
            elif not email:
                error = 'Email is requried.'

            if error is None:
                try:
                    #if details not used, create entry into database, else return error to client
                    db.execute(
                        "INSERT INTO user (username, password,email) VALUES (?, ?,?)",
                        (username, generate_password_hash(password),email),
                    )
                    db.commit()
                except db.IntegrityError:
                    error = f"User {username} is already registered."
                else:
                    #redirects client to login page
                    #return redirect(url_for("auth.userCreated"))
                    return redirect(request.url)

            flash(error)
    return render_template('auth/login_register.html')

#before app loads, check if user is login and session is created. If user is login, session is created, else proceeds with no user session
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

#function extension to route auth request for logout resource
@bp.route('/logout')
def logout():
    #clear user session
    session.clear()
    return redirect(url_for('main.index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login-register'))

        return view(**kwargs)

    return wrapped_view
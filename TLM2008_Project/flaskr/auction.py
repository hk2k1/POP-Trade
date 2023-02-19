import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auction', __name__, url_prefix='/auction')

@bp.route('/auction',methods=('GET','POST'))
def auction():
    return render_template('auction/auctionMain.html')#renders the html and returns back to caller

# @bp.route('/ping',methods=('POST'))
# def pingTest():
#     return "Hello website!"
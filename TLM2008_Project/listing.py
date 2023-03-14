from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import os

from TLM2008_Project.db import get_db

listingBp = Blueprint('listingBp',__name__,url_prefix='/listing')
print("Initializing listing.py...")

@listingBp.route("/createListing/")
def createListing():
    user_id = session.get('user_id')
    return render_template("/listing/createListing.html",user_id=user_id)
from flask import Blueprint, render_template, request
from .models import user_comments, happy_response, sad_response, content_response
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/about')
def about():
    return render_template("about.html")


@auth.route('/entries')
def entries():
    return render_template("entries.html")


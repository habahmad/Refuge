from flask import Blueprint, render_template, request, flash
from .models import user_comments, happy_response, sad_response, content_response
from . import db
from sqlalchemy.sql.expression import func

#this file has a bunch of roots/URLs defined inside it, it's a blueprint of our website

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST']) #decorator, defining root
#function will run whenever we go to above url (main page of website)
def entry():
    if request.method == "POST":
        data = request.form.get('entry') #stores entry from textbox
        new_entry = user_comments(commentContent=data)
        db.session.add(new_entry)
        db.session.commit()
        print(data)
        return render_template("index.html")
    else:
        return render_template("index.html")

@views.route('/', methods=['GET', 'POST'])
def mood():
    selected_mood = request.form.get('category')
    if selected_mood == 'happy':
        response = happy_response.query.order_by(happy_response.h_respContent).order_by(func.random()).limit(1).first()
        print(response)
    elif selected_mood == 'sad':
        response = sad_response.query.with_entities(sad_response.s_respContent).order_by(func.random()).limit(1).first()
        print(response)
    elif selected_mood == 'content':
        response = content_response.query.with_entities(content_response.c_respContent).order_by(func.random()).limit(1).first()   
        print(response) 
    else: 
        response = "No mood selected"    

    return render_template("index.html", response=response)
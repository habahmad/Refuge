from . import db
from sqlalchemy.sql import func

class user_comments(db.Model):
    commentID = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    commentContent = db.Column(db.String(500))
    time_stamp = db.Column(db.DateTime(timezone=True), default=func.now())

class happy_response(db.Model):
    h_respID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    h_respContent = db.Column(db.String(300))

class sad_response(db.Model):
    s_respID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_respContent = db.Column(db.String(300))

class content_response(db.Model):
    c_respID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_respContent = db.Column(db.String(300))
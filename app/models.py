# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime

class MovieProfile(db.Model):
    __tablename__ = 'movie_profile'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(80))
    filename =  db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, id, title, description, filename, created_at):
        self.title = title
        self.description = description
        self.filename = filename
        self.created_at = created_at
 
 
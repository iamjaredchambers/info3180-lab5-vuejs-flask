# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms.validators import InputRequired


class MovieForm():
    title = StringField('Please enter movie title', validators=[InputRequired()])
    description = StringField('Describe the movie', validators=[InputRequired()] )
    poster = FileField('Choose a file', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images Only')])


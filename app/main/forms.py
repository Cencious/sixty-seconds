from typing_extensions import Required
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField

class commentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators = [Required()])
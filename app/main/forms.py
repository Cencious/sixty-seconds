from typing_extensions import Required
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,  SubmitField, RadioField
from wtforms.validators import DataRequired

class commentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators = [DataRequired()])
    vote = RadioField('default field arguments', choices =[('1', 'upvote'), ('1', 'Downvote')])
    submit = SubmitField('SUBMIT')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [DataRequired()])
    submit = SubmitField('Submit')
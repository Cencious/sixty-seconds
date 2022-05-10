from typing_extensions import Required
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,  SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired

class commentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators = [DataRequired()])
    vote = RadioField('default field arguments', choices =[('1', 'upvote'), ('1', 'Downvote')])
    submit = SubmitField('SUBMIT')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    category_id = SelectField('Select category', choises = [('1', 'Interview'), ('2', 'Pick Up Lines'), ('3','Promotion'), ('4', 'Product')])
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('Create Pitch')

class UpvoteForm(FlaskForm):
    ''' 
    Class to create a wft form for upvoting a pitch.
    '''
    submit = SubmitField('Upvote')
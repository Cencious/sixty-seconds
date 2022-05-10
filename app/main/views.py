from flask import render_template, request, redirect, url_for, abort
from . import main
from .forms import CommentsForm, UpdateProfile, PitchForm, UpvoteForm
from ..models import Comment, Pitch, User 

@main.route('/')
def index():    
    '''
   View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The most intertactive Pitching Website'

    search_pitch = request.args.get('pitch_query')
    pitches = Pitch.get_all_pitches()

    return render_template('index.html', title = title, pitches= pitches)

#this section consist of the category root functions
@main.route('/inteview/pitches/')
def interview():
    '''
    View root page function that returns the index page and its data
    '''
    pitches= Pitch.get_all_pitches()
    title = 'Home - Welcome to The best Pitching Website Online'  
    return render_template('interview.html', title = title, pitches= pitches )
    

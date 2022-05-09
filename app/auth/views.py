from flask import render_template
from . import auth
from . import LoginForm

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()

"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('UserModel')
        self.db = self._app.db

    # Welcome page
    def index(self):
        return self.load_view('index.html')


    def registration(self):
        # grab form data (POST) & put into registration_data
        registration_data = {
                'name': request.form['name'],
                'alias': request.form['alias'],
                'email': request.form['email'],
                'password': request.form['password'],
                'confirm_password': request.form['confirm_password'],
                'birthday': request.form['birthday']
        }
        # call UserModel.create_user(registration_data)
        registration = self.models['UserModel'].create_user(registration_data)
        # check for errors, if errors, print errors
        if registration['status'] == False:
            flash(registration['errors'])
        else:
            flash("User registered!")
        return redirect('/')

    def login_validation(self):
        # grab form data (POST) and save into login_data
        login_data = {
                'email': request.form['email'],
                'password': request.form['password']
        }
        # call UserModel.check_user(login_data)
        login_status = self.models['UserModel'].check_user(login_data)

        if (login_status['status']): # if ok, store session['id'] = user_id
            session['id'] = login_status['user_id']
            return redirect('/quotes')
        else: # if not ok, then flash validation errors
            flash(login_status['errors'])
            return redirect('/')


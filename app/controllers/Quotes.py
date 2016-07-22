"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Quotes(Controller):
    def __init__(self, action):
        super(Quotes, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('UserModel')
        self.load_model('QuoteModel')
        self.db = self._app.db
   
    def index(self):
        # Grab user data
        one_user = self.models['UserModel'].get_data_by_user_id(session['id'])
        # Grab all quotes (except favorited ones)
        all_quotes = self.models['QuoteModel'].get_all_quotes(session['id'])
        # Grab all quotes (only favorited ones)
        favorite_quotes = self.models['QuoteModel'].get_all_user_favorites(session['id'])

        # render template
        return self.load_view('dashboard.html', user=one_user[0], all_quotes=all_quotes, favorite_quotes=favorite_quotes)

    def all_quotes_by_user(self, user_id):
        # Grab user information by user_id
        user = self.models['UserModel'].get_data_by_user_id(user_id)
        # Grab all quotes by the user_id
        allQuotes = self.models['QuoteModel'].get_quote_by_id(user_id)
        # Render page
        return self.load_view('user.html', user = user[0], allQuotes = allQuotes)

    def add_to_favorites(self, quote_id):
        self.models['QuoteModel'].add_to_favorites(session['id'], quote_id)
        return redirect('/quotes')

    def remove_from_favorites(self, quote_id):
        self.models['QuoteModel'].delete_from_favorites(session['id'], quote_id)
        return redirect('/quotes')

    def add_quote(self):
        quote_info = {
                    'author': request.form['author'],
                    'message': request.form['message'],
                    'poster_id': session['id']
        }
        quote_add = self.models['QuoteModel'].add_quote(quote_info)
        # check for errors, if errors, print errors
        if quote_add['status'] == False:
            flash(quote_add['errors'])
        else:
            flash("Quote Added!")
        return redirect('/quotes')

    def logout(self):
        session.clear()
        return redirect('/')
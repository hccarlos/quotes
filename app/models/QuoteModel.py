""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class QuoteModel(Model):
    def __init__(self):
        super(QuoteModel, self).__init__()

    # SELECT all quotes not favorited by user
    # returns list of quote entries (dictionary)
    ## DONE
    def get_all_quotes(self, session_user_id):
        # get all from quotes, where quotes.id not in the session user's favorite table
        query = "SELECT T1.id as quoteID, T1.author, T1.message, Posters.id as posterID, Posters.name FROM users as Posters JOIN (SELECT userQuotes.id, userQuotes.author, userQuotes.message, userQuotes.poster_id FROM quotes as userQuotes WHERE userQuotes.id NOT IN (SELECT quotes_id FROM favorites t1 JOIN users sessionUser ON sessionUser.id = t1.users_id WHERE sessionUser.id = :user_id)) as T1 ON T1.poster_id = Posters.id"
        data = {'user_id': session_user_id}
        return self.db.query_db(query, data)

    # SELECT all quotes posted by specific user
    ## DONE
    def get_quote_by_id(self, poster_id):
        # SELECT those SQL entries whose poster_id = user_id
        query = "SELECT * FROM quotes WHERE quotes.poster_id = :user_id; "
        data = { 'user_id': poster_id}
        return self.db.query_db(query, data)

    # SELECT all quotes favorited by user
    ## DONE
    def get_all_user_favorites(self, session_user_id):
        query = "SELECT T1.id as quoteID, T1.author, T1.message, Posters.id as posterID, Posters.name FROM users as Posters JOIN (SELECT userQuotes.id, userQuotes.author, userQuotes.message, userQuotes.poster_id FROM quotes as userQuotes WHERE userQuotes.id IN (SELECT quotes_id FROM favorites t1 JOIN users sessionUser ON sessionUser.id = t1.users_id WHERE sessionUser.id = :user_id)) as T1 ON T1.poster_id = Posters.id"
        data = {'user_id': session_user_id}
        return self.db.query_db(query, data)

    # Add to favorites table
    ## DONE
    def add_to_favorites(self, session_user_id, quotes_id):
        query = "INSERT INTO favorites (users_id, quotes_id) VALUES (:users_id, :quotes_id)"
        data = { 'users_id': session_user_id, 'quotes_id': quotes_id }
        return self.db.query_db(query, data)

    # Remove from favorites table
    ## DONE
    def delete_from_favorites(self, session_user_id, quotes_id):
        query = "DELETE FROM favorites WHERE (quotes_id = :quotes_id AND users_id = :user_id)"
        data = { "quotes_id": quotes_id, "user_id": session_user_id}
        return self.db.query_db(query, data)

    # Add to quotes table
    def add_quote(self, quote_info):
        allOK = True
        errors = []
        query = "INSERT INTO quotes (author, message, poster_id, created_at, updated_at) VALUES (:author, :message, :poster_id, NOW(), NOW())"
        if len(quote_info['author']) < 3:
            allOK = False
            errors.append("Author name has to be more than 3 characters")
        if len(quote_info['message']) < 10:
            allOK = False
            errors.append("Quote needs more than 10 characters")

        if allOK:
            data = {
                'author': quote_info['author'],
                'message': quote_info['message'],
                'poster_id': quote_info['poster_id']
                }
            inserted_quote_id = self.db.query_db(query, data)
            return {"status": True, "inserted_user_id": inserted_quote_id}
        else:
            return {"status": False, "errors": errors}

        return self.db.query_db(query, data)

    # def delete_quotes(self, quote_id):
    #     query = "DELETE FROM quotes WHERE id = :quotes_id"
    #     data = { "quotes_id": quote_id }
    #     return self.db.query_db(query, data)
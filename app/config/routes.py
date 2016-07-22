"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

"""
    This is where you define routes
    
    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter 
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
routes['default_controller'] = 'Users'
routes['POST']['/registration'] = 'Users#registration'
routes['POST']['/login_validation'] = 'Users#login_validation'
routes['GET']['/quotes'] = 'Quotes#index'
routes['GET']['/all_quotes_by_user/<int:user_id>'] = 'Quotes#all_quotes_by_user'
routes['GET']['/add_to_favorites/<int:quote_id>'] = 'Quotes#add_to_favorites'
routes['GET']['/remove_from_favorites/<int:quote_id>'] = 'Quotes#remove_from_favorites'
routes['GET']['/quotes/logout'] = 'Quotes#logout'
routes['POST']['/add_quote'] = 'Quotes#add_quote'

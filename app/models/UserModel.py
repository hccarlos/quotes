""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

class UserModel(Model):
    def __init__(self):
        super(UserModel, self).__init__()

    def create_user(self, registration_data):
        # Setting up REGEX patterns
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
        # PASS_REGEX = re.compile(r'(.*([A-Z]+).*([0-9]+).*)|(.*([0-9]+).*([A-Z]+).*)')
        # errors message list instantiation
        errors=[]
        # Do checks
        allOK = True
        #extract all the data and save into session dictionary
        temp_email = registration_data['email']
        temp_name = registration_data['name']
        temp_alias = registration_data['alias']
        temp_pass = registration_data['password']
        temp_pass2 = registration_data['confirm_password']
        temp_bday = registration_data['birthday']
        #check email and flash accordingly
        if len(temp_email) < 1:
            errors.append("Email cannot be blank!")
            allOK = False
        if not EMAIL_REGEX.match(temp_email):
            errors.append("Invalid Email Address!")
            allOK = False

        #check name and flash accordingly
        if len(temp_name) < 1:
            errors.append("First Name cannot be blank!")
            allOK = False
        if not temp_name.isalpha():
            errors.append("Invalid First Name! Cannot contain numbers")
            allOK = False

        #check alias and flash accordingly
        if len(temp_alias) < 1:
            errors.append("Alias cannot be blank!")
            allOK = False

        #check passwords and flash accordingly
        if len(temp_pass) < 1:
            errors.append("Password cannot be blank!")
            allOK = False
        if len(temp_pass) < 8:
            errors.append("Password should be more than 8 characters!")
            allOK = False
        # if not PASS_REGEX.match(temp_pass):
        #     errors.append("Invalid Password! Must have 1 uppercase letter and 1 numeric value")
        #     allOK = False
        if temp_pass != temp_pass2:
            errors.append("Password and confirmation must match")
            allOK = False


        #if all pass, hash password, then insert data into database
        if allOK:
            hash_pw = self.bcrypt.generate_password_hash(temp_pass)
            query = "INSERT INTO users (name, alias, email, password, created_at, updated_at, birthday) VALUES (:name, :alias, :email, :hpass, NOW(), NOW(), :birthday)"
            data = {'name': temp_name,
                    'alias': temp_alias,
                    'hpass': hash_pw,
                    'email': temp_email,
                    'birthday': temp_bday
            }
            inserted_user_id = self.db.query_db(query, data)
            return {"status": True, "inserted_user_id": inserted_user_id}
        else:
            return {"status": False, "errors": errors}



    def check_user(self, login_data):
        # extract data passed in from validate() in Login.py
        email = login_data['email']
        password = login_data['password']
        # pull that password data from DB based on email, and match against password
        if (email > 0) and (password > 0):
            query = "SELECT * FROM users WHERE email = :email LIMIT 1"
            data = {'email': email}
            user = self.db.query_db(query, data)
            
            # if no user with that email found
            if not user:
                return {"status": False, "errors": ["No such user registered"]}
            
            # if password matches, then return the user
            if self.bcrypt.check_password_hash(user[0]['password'], password):
                return {"status": True,"user_id": user[0]['id']}
            # or if password doesn't match
            else:
                return {"status": False,"errors": ["email or password incorrect"]}
        
        else:
            return {"status": False, "errors": ["No password or no email entered"]}



# return data on a single user
    def get_data_by_user_id(self, user_id):
        query = "SELECT * FROM users WHERE id = :user_id"
        data = {
                'user_id': user_id
        }
        one_user = self.db.query_db(query, data)
        return one_user
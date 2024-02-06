from model.da.user_da import *
from tools.Validator import *
from model.entity.user import User
from model.entity.post import Post
from model.entity.comment import Comment


class UserController:

    def save(self, name, family, username, password, status=True):
        try:
            if name_validator(name) and name_validator(family) and username_validator(username):
                user = User(name, family, username, password, status=True)
                da = UserDa()
                da.save(user)
                return "Saved"
            else:
                raise ValueError("Invalid Data")
        except Exception as e:
            return str(e)

    def edit(self, id, name, family, username, password, status):
        try:
            if name_validator(name) and name_validator(family) and user_id_validator(id):
                da = UserDa()
                user = da.find_by_id(User, id)
                user.name = name
                user.family = family
                user.username = username
                user.password = password
                user.status = status
                da.edit(user)
                return "Edited"
            else:
                raise ValueError("Invalid Data")
        except Exception as e:
            return str(e)

    def remove(self, id):
        try:
            if user_id_validator(id):
                da = UserDa()
                da.remove_by_id(User, id)
                return "Removed"
            else:
                raise ValueError("User Doesn't Exist!!!")
        except Exception as e:
            return str(e)

    def find_all(self):
        try:
            da = UserDa()
            return da.find_all(User)
        except Exception as e:
            return str(e)

    def find_by_id(self, id):
        try:
            da = UserDa()
            if da.find_by_id(User, id):
                return da.find_by_id(User, id)
            else:
                raise ValueError("User Doesnt Exist")
        except Exception as e:
            return str(e)

    def find_by_id_internal(self, id):
        try:
            da = UserDa()
            if da.find_by_id_internal(User, id):
                return da.find_by_id_internal(User, id)
            else:
                raise ValueError("User Doesnt Exist")
        except Exception as e:
            return str(e)

    def find_by_username(self, username):
        try:
            da = UserDa()
            if da.find_by_username(User, username):
                return da.find_by_username(User, username)
            else:
                raise ValueError("Username Doesn't Exist!!!")
        except Exception as e:
            return str(e)

    def find_by_username_and_password(self, username, password):
        try:
            da = UserDa()
            if da.find_by_username_and_password(User, username, password):
                return da.find_by_username_and_password(User, username, password)
            else:
                raise ValueError("Username or Password Doesn't Exist!!!")
        except Exception as e:
            return str(e)

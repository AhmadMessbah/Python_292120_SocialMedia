from model.da.user_da import *
from tools.Validator import *
from model.entity.user import User
from model.entity.post import Post
from model.entity.comment import Comment


class UserController:
    def save(self, name, family, username, password, status=True):
        try:
            if name_validator(name) and name_validator(family):
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
            if name_validator(name) and name_validator(family):
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
        pass

    def find_all(self):
        pass

    def find_by_id(self, id):
        try:
            da = UserDa()
            return da.find_by_id(User, id)

        except Exception as e:
            return str(e)

    def find_by_username(self, username):
        pass

    def find_by_username_and_password(self, username, password):
        pass

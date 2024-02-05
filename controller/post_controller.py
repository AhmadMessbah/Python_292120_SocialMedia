from model.entity.user import User
from model.entity.post import Post
from model.entity.comment import Comment
from model.entity.like import Like
from model.da.post_da import *

class PostController:

    def save(self, text, user):
        try:
            post = Post(text, user)
            da = PostDa()
            da.save(post)
            return "Saved"
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
        try:

            da = UserDa()
            if da.find_by_id(User, id):
                da.remove_by_id(User, id)
                return "Removed"
            else:
                raise ValueError("Item Not Found!!!")
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
            return da.find_by_id(User, id)
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

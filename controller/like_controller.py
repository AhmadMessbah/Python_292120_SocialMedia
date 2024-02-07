from datetime import datetime
from model.entity.user import User
from model.entity.post import Post
from model.entity.comment import Comment
from model.entity.like import Like
from model.da.like_da import *


class LikeController:

    def save(self, post, user):
        try:
            like = Like(post, user)
            da = LikeDa()
            da.save(like)
            return "Saved"
        except Exception as e:
            return str(e)

    def edit(self, id, post, user):
        try:
            da = LikeDa()
            like = da.find_by_id(Like, id)
            like.post = post
            like.user = user
            like.date_time = datetime.now()
            da.edit(like)
            return "Edited"
        except Exception as e:
            return str(e)

    def remove(self, id):
        try:
            da = LikeDa()
            if da.find_by_id(Like, id):
                da.remove_by_id(Like, id)
                return "Removed"
            else:
                raise ValueError("Like Doesnt Exist!!!")
        except Exception as e:
            return str(e)


    def find_all(self):
        try:
            da = LikeDa()
            return da.find_all(Like)
        except Exception as e:
            return str(e)


    def find_by_id(self, id):
        try:
            da = LikeDa()
            return da.find_by_id(Like, id)
        except Exception as e:
            return str(e)

    def find_by_id_internal(self, id):
        try:
            da = LikeDa()
            return da.find_by_id_internal(Like, id)
        except Exception as e:
            return str(e)

    def find_by_user(self, user):
        try:
            da = LikeDa()
            if da.find_by_user(Like, user):
                return da.find_by_user(Like, user)
            else:
                raise ValueError("User Doesn't Exist!!!")
        except Exception as e:
            return str(e)

    def find_by_post(self, post):
        try:
            da = LikeDa()
            if da.find_by_post(Like, post):
                return da.find_by_post(Like,post)
            else:
                raise ValueError("Post Doesn't Exist!!!")
        except Exception as e:
            return str(e)

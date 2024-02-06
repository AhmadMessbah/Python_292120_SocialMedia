from datetime import datetime
from model.da.user_da import UserDa
from model.entity.user import User
from model.entity.post import Post
from model.entity.comment import Comment
from model.entity.like import Like
from model.da.post_da import *
from tools.Validator import text_validator, post_id_validator, user_id_validator


class PostController:

    def save(self, text, user):
        try:
            if text_validator(text):
                post = Post(text, user)
                da = PostDa()
                da.save(post)
                return "Saved"
            else:
                raise ValueError
        except Exception as e:
            return str(e)

    # def edit(self, id, text, user):
    #     try:
    #         if text_validator(text) and user_validator(user) and post_id_validator(id):
    #             da = PostDa()
    #             post = da.find_by_id(Post, id)
    #             post.user = user
    #             post.text = text
    #             post.date_time = datetime.now()
    #             da.edit(post)
    #             return "Edited"
    #         else:
    #             raise ValueError
    #     except Exception as e:
    #         return str(e)
    #
    # def remove(self, id):
    #     try:
    #         if post_id_validator(id):
    #             da = PostDa()
    #             if da.find_by_id(Post, id):
    #                 da.remove_by_id(Post, id)
    #                 return "Removed"
    #         else:
    #             raise ValueError
    #     except Exception as e:
    #         return str(e)
    #
    # def find_all(self):
    #     try:
    #         da = PostDa()
    #         return da.find_all(Post)
    #     except Exception as e:
    #         return str(e)
    #
    # def find_by_id(self, id):
    #     try:
    #         da = PostDa()
    #         return da.find_by_id(Post, id)
    #     except Exception as e:
    #         return str(e)
    #
    # def find_by_id_internal(self, id):
    #     try:
    #         da = PostDa()
    #         return da.find_by_id_internal(Post, id)
    #     except Exception as e:
    #         return str(e)
    #
    # def find_by_user(self, user):
    #     try:
    #         da = PostDa()
    #         if da.find_by_user(Post, user):
    #             return da.find_by_user(Post, user)
    #         else:
    #             raise ValueError("User Doesn't Exist!!!")
    #     except Exception as e:
    #         return str(e)
    #
    # def find_by_text(self, text):
    #     try:
    #         da = PostDa()
    #         if da.find_by_text(Post, text):
    #             return da.find_by_text(Post, text)
    #         else:
    #             raise ValueError("Post Doesn't Exist!!!")
    #     except Exception as e:
    #         return str(e)

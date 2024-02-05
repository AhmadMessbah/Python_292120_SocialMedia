from datetime import datetime
from model.entity.user import User
from model.entity.post import Post
from model.entity.comment import Comment
from model.entity.like import Like
from model.da.comment_da import *


class CommentController:

    def save(self, text, post, user):
        try:
            comment = Comment(text,post, user)
            da = CommentDa()
            da.save(comment)
            return "Saved"
        except Exception as e:
            return str(e)

    def edit(self, id, text, post, user):
        try:
            da = CommentDa()
            comment = da.find_by_id(Comment, id)
            comment.post = post
            comment.user = user
            comment.text=text
            comment.date_time = datetime.now()
            da.edit(comment)
            return "Edited"
        except Exception as e:
            return str(e)

    def remove(self, id):
        try:
            da = CommentDa()
            if da.find_by_id(Comment, id):
                da.remove_by_id(Comment, id)
                return "Removed"
            else:
                raise ValueError("Comment Doesnt Exist!!!")
        except Exception as e:
            return str(e)


    def find_all(self):
        try:
            da = CommentDa()
            return da.find_all(Comment)
        except Exception as e:
            return str(e)


    def find_by_id(self, id):
        try:
            da = CommentDa()
            return da.find_by_id(Comment, id)
        except Exception as e:
            return str(e)

    def find_by_id_internal(self, id):
        try:
            da = CommentDa()
            return da.find_by_id_internal(Comment, id)
        except Exception as e:
            return str(e)

    def find_by_user(self, user):
        try:
            da = CommentDa()
            if da.find_by_user(Comment, user):
                return da.find_by_user(Comment, user)
            else:
                raise ValueError("User Doesn't Exist!!!")
        except Exception as e:
            return str(e)

    def find_by_post(self, post):
        try:
            da = CommentDa()
            if da.find_by_post(Comment, post):
                return da.find_by_post(Comment,post)
            else:
                raise ValueError("Post Doesn't Exist!!!")
        except Exception as e:
            return str(e)

    def find_by_text(self, text):
        try:
            da = CommentDa()
            if da.find_by_text(Comment, text):
                return da.find_by_text(Comment, text)
            else:
                raise ValueError("Comment Doesn't Exist!!!")
        except Exception as e:
            return str(e)
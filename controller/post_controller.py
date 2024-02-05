from datetime import datetime
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

    def edit(self, id, text, user):
        try:
            da = PostDa()
            post = da.find_by_id(Post, id)
            if len(text)<30:
                post.user = user
                post.text = text
                post.date_time = datetime.now()
                da.edit(post)
                return "Edited"
            else:
                raise ValueError("Text Too Long")
        except Exception as e:
            return str(e)

    def remove(self, id):
        try:
            da = PostDa()
            if da.find_by_id(Post, id):
                da.remove_by_id(Post, id)
                return "Removed"
            else:
                raise ValueError("Post Doesnt Exist!!!")
        except Exception as e:
            return str(e)


    def find_all(self):
        try:
            da = PostDa()
            return da.find_all(Post)
        except Exception as e:
            return str(e)


    def find_by_id(self, id):
        try:
            da = PostDa()
            return da.find_by_id(Post, id)
        except Exception as e:
            return str(e)

    def find_by_id_internal(self, id):
        try:
            da = PostDa()
            return da.find_by_id_internal(Post, id)
        except Exception as e:
            return str(e)

    def find_by_user(self, user):
        try:
            da = PostDa()
            if da.find_by_user(Post, user):
                return da.find_by_user(Post, user)
            else:
                raise ValueError("User Doesn't Exist!!!")
        except Exception as e:
            return str(e)

    def find_by_text(self, text):
        try:
            da = PostDa()
            if da.find_by_text(Post, text):
                return da.find_by_text(Post,text)
            else:
                raise ValueError("Post Doesn't Exist!!!")
        except Exception as e:
            return str(e)

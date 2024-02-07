import re
from model.da.database_manager import DatabaseManager
from model.entity.user import User
from model.entity.post import Post
from model.entity.like import Like
from model.entity.comment import Comment




def post_id_validator(x):
    db = DatabaseManager()
    if db.find_by_id_internal(Post, x):
        return True
    else:
        raise ValueError("Post Doesn't Exist!!!")



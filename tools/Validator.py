import re
from model.da.database_manager import DatabaseManager
from model.entity import user
from model.entity.user import User
from model.entity.post import Post
from model.entity.comment import Comment


def name_validator(x):
    return bool(re.match("^[A-Za-z\s]{2,20}$", x, re.I))


def username_validator(x):
    db = DatabaseManager()
    if not db.find_by_username(User, x):
        return True
    else:
        raise ValueError("Duplicate Username")


def user_validator(x):
    try:
        db = DatabaseManager()
        if db.find_by_id_internal(User, x.id):
            return True
        else:
            raise ValueError("User Doesn't Exist!!!")
    except Exception as e:
            raise ValueError("User Doesn't Exist!!!")

def text_validator(x):
        if len(x)<30:
            return True
        else:
            raise ValueError("Text Too Long!!")

#
# db = DatabaseManager()
# user = db.find_by_id_internal(User, 90)
# print(user_validator(user))

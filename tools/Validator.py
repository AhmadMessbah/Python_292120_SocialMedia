import re
from model.da.database_manager import DatabaseManager
from model.entity.user import User


def name_validator(x):
    return bool(re.match("^[A-Za-z\s]{2,20}$", x, re.I))


def username_validator(x):
    db = DatabaseManager()
    if not db.find_by_username(User, x):
        return True
    else:
        raise ValueError("Duplicate Username")


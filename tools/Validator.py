import re


def name_validator(x):
    return bool(re.match("^[A-Za-z\s]{2,20}$", x, re.I))


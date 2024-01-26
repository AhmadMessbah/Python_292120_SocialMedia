from datetime import datetime


class Post:
    def __init__(self, text, date_time, user):
        self.id = None
        self.text = text
        self.date_time = datetime.now()
        self.user = user

    def __repr__(self):
        return str(self.__dict__)

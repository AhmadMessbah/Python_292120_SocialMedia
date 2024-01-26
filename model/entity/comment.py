from datetime import datetime


class Comment(Base):
    def __init__(self, text, post, user, date_time):
        self.id = None
        self.text = text
        self.post = post
        self.user = user
        self.date_time = datetime.now()

    def __repr__(self):
        return str(self.__dict__)

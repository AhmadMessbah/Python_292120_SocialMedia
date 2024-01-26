from datetime import datetime


class Like(Base):
    def __init__(self, post, user, date_time):
        self.id = None
        self.post = post
        self.user = user
        self.date_time = datetime.now()

    def __repr__(self):
        return str(self.__dict__)

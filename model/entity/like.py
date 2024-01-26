from datetime import datetime


class Like:
    def __init__(self, post, user, date_time):
        self.id = None
        self.post = post
        self.user = user
        self.date_time = datetime.now()

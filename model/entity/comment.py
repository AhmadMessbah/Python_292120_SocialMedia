from datetime import datetime


class Comment:
    def __init__(self, text, post, user, date_time):
        self.id = None
        self.text = text
        self.post = post
        self.user = user
        self.date_time = datetime.now()

from datetime import datetime


class Chat:
    def __init__(self, text, date_time, sender, receiver):
        self.id = None
        self.text = text
        self.date_time = datetime.now()
        self.sender = sender
        self.receiver = receiver

    def __repr__(self):
        return str(self.__dict__)

from model.entity.base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Chat(Base):
    __tablename__ = "chat_tbl"
    id = Column(Integer, primary_key=True)
    sender = Column(String(30))
    reciever = Column(String(30))
    text = Column(String(30))

    def __init__(self, text,sender, receiver):
        self.text = text
        self.sender = sender
        self.receiver = receiver

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base

class Post(Base):
    __tablename__ = "post_tbl"
    id = Column(Integer, primary_key=True)
    text = Column(String(30))
    date_time = Column(DateTime)

    user_id = Column(Integer, ForeignKey("user_tbl.id"), nullable="True")
    user = relationship("User", back_populates="posts")

    comments = relationship("Comment", back_populates="post")

    def __init__(self, text, user):
        self.text = text
        self.date_time = datetime.now()
        self.user = user


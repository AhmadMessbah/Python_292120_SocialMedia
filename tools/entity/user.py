from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from tools.entity.base import Base


class User(Base):
    __tablename__ = "user_tbl"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    username = Column(String(30))
    password = Column(String(30))
    status = Column(Boolean)
    #posts = relationship("Post", back_populates="user")

    def __init__(self, name, family, username, password, status=True):
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.status = status

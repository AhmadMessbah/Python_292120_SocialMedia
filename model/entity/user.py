from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from model.entity.base import Base



class User(Base):
    __tablename__ = "user_tbl"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    username = Column(String(30))
    password = Column(String(30))
    status = Column(Boolean)

    posts = relationship("Post", back_populates="user", cascade="delete-orphan")
    comments = relationship("Comment", back_populates="user", cascade="delete-orphan")
    like = relationship("Like", back_populates="user", cascade="delete-orphan")

    def __init__(self, name, family, username, password, status=True):
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.status = status

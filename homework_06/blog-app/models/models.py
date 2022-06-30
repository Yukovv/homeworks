from sqlalchemy import Column, String, Integer, ForeignKey

from .database import db


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String)

    posts = db.relationship("Post", back_populates="user", cascade='all, delete-orphan', passive_deletes=True)


class Post(db.Model):
    __tablename__ = 'posts'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable=False, unique=False)
    title = Column(String, nullable=False, default="", server_default="")
    body = Column(String, nullable=False, default="", server_default="")

    user = db.relationship("User", back_populates="posts")

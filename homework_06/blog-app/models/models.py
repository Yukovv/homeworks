from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, declared_attr

from .database import db


class Base(db.Model):

    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)


class User(Base):
    name = Column(String)
    username = Column(String, unique=True)
    email = Column(String)

    posts = relationship("Post", back_populates="user")


class Post(Base):
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=False)
    title = Column(String, nullable=False, default="", server_default="")
    body = Column(String, nullable=False, default="", server_default="")

    user = relationship("User", back_populates="posts")

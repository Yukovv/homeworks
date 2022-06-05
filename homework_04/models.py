"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, declared_attr

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://username:passwd!@127.0.0.1:5433/blog"


engine = create_async_engine(PG_CONN_URI)
Session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


class Base:

    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)


Base = declarative_base(bind=engine, cls=Base)


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

"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from homework_04.jsonplaceholder_requests import fetch_json, USERS_DATA_URL, POSTS_DATA_URL
from homework_04.models import engine, Base, Session, User, Post


async def create_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


async def drop_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)


async def create_users(session: AsyncSession, users_data: list[dict]) -> list[User]:

    users = []
    for usr in users_data:
        user = User(name=usr['name'], username=usr['username'], email=usr['email'])
        users.append(user)

    session.add_all(users)
    await session.commit()

    return users


async def create_posts(session: AsyncSession, posts_data: list[dict]) -> list[Post]:

    posts = []
    for pst in posts_data:
        post = Post(user_id=pst['userId'], title=pst['title'], body=pst['body'])
        posts.append(post)

    session.add_all(posts)
    await session.commit()

    return posts


async def async_main():
    await drop_tables()  # fine
    await create_tables()  # this step is fine!

    users_data: list[dict]
    posts_data: list[dict]
    users_data, posts_data = await asyncio.gather(
        fetch_json(USERS_DATA_URL),
        fetch_json(POSTS_DATA_URL),
    )

    for usr in users_data:
        print(usr)
    print()
    for pst in posts_data:
        print(pst)

    async with Session() as session:
        await create_users(session, users_data)
        await create_posts(session, posts_data)


def main():
    asyncio.get_event_loop().run_until_complete(async_main())


if __name__ == "__main__":
    main()

"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio

import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def query_users():
    async with aiohttp.ClientSession() as session:
        async with session.get(USERS_DATA_URL) as resp:
            print(resp.status)
            print(resp.text)


async def query_posts():
    async with aiohttp.ClientSession() as session:
        async with session.get(POSTS_DATA_URL) as resp:
            print(resp.status)
            print(resp.text)


async def fetch_json(url: str) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data: list[dict] = await resp.json()

            return data

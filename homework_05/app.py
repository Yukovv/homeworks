"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.get("/", endpoint="index")
def index_view():
    return render_template("base.html")


@app.get("/about/", endpoint="about")
def about_page():
    return """One day the Hare laughed at the short feet and slow speed of the Tortoise. The Tortoise replied: "You may be as fast as the wind, but I will beat you in a race!" The Hare thought this idea was impossible and he agreed to the proposal. It was agreed that the Fox should choose the course and decide the end. The day for the race came, and the Tortoise and Hare started together. The Tortoise never stopped for a moment, walking slowly but steadily, right to the end of the course. The Hare ran fast and stopped to lie down for a rest. But he fell fast asleep. Eventually, he woke up and ran as fast as he could. But when he reached the end, he saw the Tortoise there already, sleeping comfortably after her effort."""


if __name__ == "__main__":
    app.run(debug=True)

from os import getenv

from flask import Flask, request, render_template, flash, url_for
from flask_migrate import Migrate

from models.database import db
from models import User, Post

app = Flask(__name__)
config_name = "config.%s" % getenv("Config", "DevelopmentConfig")
app.config.from_object(config_name)

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)


@app.route("/", endpoint="index")
def index_page():
    return render_template("index.html")


@app.get("/users/", endpoint="users")
def users_list():
    users = User.query.all()
    return render_template("list.html", elements_list=users, list_name="users")


@app.get("/posts/", endpoint="posts")
def posts_list():
    posts = Post.query.all()
    return render_template("list.html", elements_list=posts, list_name="posts")

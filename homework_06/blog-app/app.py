from os import getenv

from flask import Flask, request, render_template, flash, url_for
from flask_migrate import Migrate
from werkzeug.exceptions import NotFound

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


@app.route("/posts/<int:post_id>", methods=["GET", "DELETE"], endpoint="post_details")
def get_post_by_id(post_id: int):
    post = Post.query.get(post_id)
    if post is None:
        raise NotFound(f"Post #{post_id} not found!")

    if request.method == "GET":
        return render_template("post_details", post=post)


@app.route("/users/<int:post_id>", methods=["GET", "DELETE"], endpoint="user_details")
def get_user_by_id(user_id: int):
    user = User.query.get(user_id)
    if user is None:
        raise NotFound(f"User #{user_id} not found!")

    if request == "GET":
        return render_template("user_details", user=user)



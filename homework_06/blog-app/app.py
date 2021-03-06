import logging
from os import getenv

from flask import Flask, request, render_template, flash, url_for
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError, DatabaseError
from werkzeug.exceptions import NotFound, InternalServerError
from werkzeug.utils import redirect

from models.database import db
from models import User, Post
from forms import UserForm, PostForm

app = Flask(__name__)
config_name = "config.%s" % getenv("Config", "DevelopmentConfig")
app.config.from_object(config_name)

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)

log = logging.getLogger(__name__)


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


@app.route("/posts/<int:element_id>", methods=["GET", "DELETE"], endpoint="post_details")
def get_post_by_id(element_id: int):
    post = Post.query.get(element_id)
    if post is None:
        raise NotFound(f"Post #{element_id} not found!")

    if request.method == "GET":
        return render_template("post_details.html", post=post)

    title = post.title
    user_id = post.user.id
    db.session.delete(post)
    db.session.commit()
    flash(f"Deleted post {title!r}", category="warning")
    url = url_for('user_details', element_id=user_id)
    return {"ok": True, "url": url}


@app.route("/users/<int:element_id>", methods=["GET", "DELETE"], endpoint="user_details")
def get_user_by_id(element_id: int):
    user = User.query.get(element_id)
    if user is None:
        raise NotFound(f"User #{element_id} not found!")

    if request.method == "GET":
        return render_template("user_details.html", user=user)

    username = user.username
    db.session.delete(user)
    db.session.commit()
    flash(f"Deleted user {username!r}", category="warning")
    url = url_for('users')
    return {"ok": True, "url": url}


@app.route("/add_user/", methods=["GET", "POST"], endpoint="add_user")
def add_user():
    form = UserForm()
    if request.method == "GET":
        return render_template("add_user.html", form=form)

    username = form.username.data
    email = form.email.data

    user = User(username=username, email=email)
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        error_text = f"Could not save user {username!r}, probably this name is not unique"
        form.form_errors.append(error_text)
        return render_template("add_user.html", form=form), 400
    except DatabaseError:
        log.exception("could not save user %r", username)
        raise InternalServerError(f"could not save user {username!r}")

    flash(f"Created new user: {username}", category="success")
    url = url_for("users")
    return redirect(url)


@app.route("/<int:user_id>/add_post/", methods=["GET", "POST"], endpoint="add_post")
def add_post(user_id: int):
    user = User.query.get(user_id)
    if user is None:
        raise NotFound(f"User #{user_id} not found!")

    form = PostForm()
    if request.method == "GET":
        return render_template("add_post.html", form=form)

    title = form.title.data
    body = form.body.data

    post = Post(user_id=user_id, title=title, body=body)
    db.session.add(post)
    try:
        db.session.commit()
    except IntegrityError:
        error_text = f"Could not save post {title!r}, probably this title is not unique"
        form.form_errors.append(error_text)
        return render_template("add_user.html", form=form), 400
    except DatabaseError:
        log.exception("could not save post %r", title)
        raise InternalServerError(f"could not save user {title!r}")

    flash(f"Created new post: {title!r}", category="success")
    url = url_for('user_details', element_id=user_id)
    return redirect(url)


if __name__ == "__main__":
    app.run()
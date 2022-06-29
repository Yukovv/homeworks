from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField(
        label="Post title",
        name="title",
        validators=[DataRequired()]
    )

    body = StringField(
        label="Post body",
        name="body",
        default="Some text",
    )

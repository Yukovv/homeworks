from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    username = StringField(
        label="User username",
        name="username",
        validators=[DataRequired()]
    )

    email = StringField(
        label="User email",
        name="email",
        validators=[DataRequired()]
    )
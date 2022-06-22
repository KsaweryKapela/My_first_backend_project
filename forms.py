from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[validators.Email()])
    password = PasswordField('Password', validators=[validators.InputRequired()])
    name = StringField('Name', validators=[validators.InputRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[validators.Email()])
    password = PasswordField('Password', validators=[validators.InputRequired()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = CKEditorField('Comment', validators=[validators.InputRequired()])
    submit = SubmitField('AddComment')

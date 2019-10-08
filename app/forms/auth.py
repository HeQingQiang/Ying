# coding=utf-8
"""
    Created By shineYu On 2019/9/19 15:38
"""
from wtforms import StringField, PasswordField, Form
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo

from app.models.user import User

__author__ = 'shineY'


class RegisterForm(Form):
    email = StringField(validators=[
        DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请重新输入'), Length(6, 32)])
    nickname = StringField(validators=[
        DataRequired(), Length(2, 10, message='昵称至少两个字符，最多10个字符')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')


class EmailForm(Form):
    email = StringField(validators=[
        DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])


class LoginForm(EmailForm):
    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请重新输入'), Length(6, 32)])


class ResetPasswordForm(Form):
    password = PasswordField(validators=[
        DataRequired(),
        Length(6, 32, message='密码长度至少需要在6到32个字符之间'),
        EqualTo('password2', message='两次输入的密码不相同')])
    password2 = PasswordField(validators=[
        DataRequired(), Length(6, 32)])



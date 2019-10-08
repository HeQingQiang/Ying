# coding=utf-8
"""
    Created By shineYu On 2019/9/13 6:56
"""
from flask import Blueprint, render_template

__author__ = 'shineY'

web = Blueprint('web', __name__)


@web.app_errorhandler(404)
def not_found(e):
    # AOP 面向切面编程
    return 'not found', 404


@web.app_errorhandler(500)
def not_found(e):
    return render_template('500.html'), 500


from app.web import book
from app.web import user
from app.web import auth
from app.web import gift
from app.web import main
from app.web import wish
from app.web import drift


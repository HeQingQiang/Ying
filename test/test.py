# coding=utf-8
"""
    Created By shineYu On 2019/9/13 19:00
"""
from flask import Flask, current_app

__author__ = 'shineY'


app = Flask(__name__)


a = current_app
d = current_app.config['DEBUG']

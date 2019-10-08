# coding=utf-8
"""
    Created By shineYu On 2019/9/21 13:30
"""
from threading import Thread

from flask import current_app, render_template
from flask_mail import Message

from app import mail

__author__ = 'shineY'


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件', sender='845196784@qq.com', body='调皮一下，开心就好！',
    #               recipients=['quanying@houhan.com'])
    msg = Message('[话语]'+' '+subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()


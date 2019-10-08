# coding=utf-8
"""
    Created By shineY On 2019/9/12 23:55
"""

from flask import Flask, make_response
# from config import DEBUG

__author__ = 'shineY'

app = Flask(__name__)
app.config.from_object('config')
# print(app.config['DEBUG'])


@app.route("/hello")
def hello():
    headers = {
        'content-type': 'text/plain',
        'location': 'http://www.baidu.com'
    }
    # response = make_response('<html></html>', 301)
    # response.headers = headers
    return '<html></html>', 301, headers
# app.add_url_rule('/hello', view_func=hello)


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=8080)


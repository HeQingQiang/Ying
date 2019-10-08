# coding=utf-8
"""
    Created By shineY On 2019/9/12 23:55
"""

from app import create_app

__author__ = 'shineY'

app = create_app()


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=8080)


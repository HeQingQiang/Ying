# coding=utf-8
"""
    Created By shineYu On 2019/9/13 2:30
"""
from flask import jsonify, request, render_template, flash
from flask_login import current_user

from app.forms.book import SearchForm
from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.book import BookCollection, BookViewModel
from app.view_models.trade import TradeInfo
from . import web
from app.spider.book import Book
from app.lib.helper import is_isbn_or_key

__author__ = 'shineY'


@web.route("/book/search/")
def search():
    """
    :param q: 普通关键字 isbn
    :param page: 分页参数
    :return:
    """
    form = SearchForm(request.args)
    books = BookCollection()

    # 验证层
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        book = Book()

        if isbn_or_key == 'isbn':
            book.search_by_isbn(q)
        else:
            book.search_by_keyword(q, page)

        # 返回序列化结果
        books.fill(book, q)
        # return jsonify(books.__dict__)
        # return json.dumps(books, default=lambda o: o.__dict__)
    else:
        # return jsonify(form.errors)
        flash('搜索的关键字不符合要求，请重新输入关键字。')
    return render_template('search_result.html', books=books, form=form)


@web.route("/test")
def test():
    r = {
        'name': '莹宝',
        'age': 18
    }
    flash('hello world', )
    return render_template('test.html', data=r)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False

    # 取书籍详情数据
    book = Book()
    book.search_by_isbn(isbn)
    book_result = BookViewModel(book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    return render_template('book_detail.html', book=book_result,
                           wishes=[trade_wishes_model], gifts=[trade_gifts_model],
                           has_in_wishes=has_in_wishes, has_in_gifts=has_in_gifts)


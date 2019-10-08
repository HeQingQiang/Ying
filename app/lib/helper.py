# coding=utf-8
"""
    Created By shineY On 2019/9/13 1:21
"""

__author__ = 'shineY'


def is_isbn_or_key(word):
    """
    判断输入的是关键字还是isbn
    :param word: 输入
    :return: isbn_or_key
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    sort_word = word.replace('-', '')
    if '-' in word and len(sort_word) == 10 and sort_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key


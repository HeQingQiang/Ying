# coding=utf-8
"""
    Created By shineYu On 2019/9/21 16:31
"""
from enum import Enum

__author__ = 'shineY'


class PendingStatus(Enum):
    """
        交易状态
    """
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4

    @classmethod
    def pending_str(cls, status, key):
        key_map = {
            cls.Waiting: {
                'requester': '等待对方邮寄',
                'giver': '等待你邮寄'
            },
            cls.Reject: {
                'requester': '对方已拒绝',
                'giver': '你已拒绝'
            },
            cls.Redraw: {
                'requester': '你已撤销',
                'giver': '对方已撤销'
            },
            cls.Success: {
                'requester': '对方已邮寄',
                'giver': '你已邮寄，交易完成'
            }
        }
        return key_map[status][key]


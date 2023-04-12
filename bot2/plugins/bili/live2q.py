#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/18 14:20
@author: 0xchang
@E-mail: oxchang@163.com
@file: live_to_q.py
@Github: https://github.com/0xchang
"""
import time


def live_bye(name: str, pnum: int, startime: int):
    spendtime = int(time.time() - startime)
    second = spendtime % 60
    minute = int(spendtime / 60) % 60
    hour = int(spendtime / 3600)
    mess = '【下播提醒】\n' + name + '下播了喵,谢谢观看\n' + '本次直播人气峰值: %d\n' % pnum + '本次直播时长为%s小时%s分钟%s秒\n' % (
        hour, minute, second) + '希望大家多来看我哦!'
    return mess

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
    mess = f'【下播提醒】\n{name}下播了喵,谢谢观看\n本次直播人气峰值: {pnum}\n本次直播时长为{hour}小时{minute}分钟{second}秒\n希望大家多来看我哦!'
    return mess

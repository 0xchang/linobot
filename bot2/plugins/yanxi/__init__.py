#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/14 11:11
@author: 0xchang
@E-mail: oxchang@163.com
@file: __init__.py.py
@Github: https://github.com/0xchang
"""
import time

from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_fullmatch
from .aioget import getdata


# 设置命令间隔时长为3
def time_check(nowTime, beforeTime):
    if nowTime - beforeTime > 3:
        return False
    else:
        return True


shyl = on_fullmatch('社会语录', priority=120)
histoday = on_fullmatch('历史上的今天', priority=120)
sjyl = on_fullmatch('随机语录', priority=120)
tgrj = on_fullmatch('舔狗日记', priority=120)
xljt = on_fullmatch("心灵鸡汤", priority=120)

yanxihelp = on_fullmatch('言溪帮助')


@yanxihelp.handle()
async def _():
    helpmenu = '''
    ***言溪帮助***
社会语录
历史上的今天
随机语录
舔狗日记
心灵鸡汤'''
    await yanxihelp.finish(helpmenu)


histoday_time = 0


@histoday.handle()
async def _():
    global histoday_time
    if time_check(time.time(), histoday_time):
        return
    else:
        shyltxt = await getdata('http://yanxi520.cn/api/today.php')
        histoday_time = time.time()
        await histoday.finish(Message('%s' % shyltxt))


shyl_time = 0


@shyl.handle()
async def _():
    global shyl_time
    print(shyl_time)
    if time_check(time.time(), shyl_time):
        return
    else:
        shyltxt = await getdata('http://yanxi520.cn/api/shehui.php')
        shyl_time = time.time()
        await shyl.finish(Message('%s' % shyltxt), at_sender=True)


sjyl_time = 0


@sjyl.handle()
async def _():
    global sjyl_time
    if time_check(time.time(), sjyl_time):
        return
    else:
        sjyltxt = await getdata('http://yanxi520.cn/api/yan.php')
        sjyl_time = time.time()
        await sjyl.finish(Message('%s' % sjyltxt), at_sender=True)


tgrj_time = 0


@tgrj.handle()
async def _():
    global tgrj_time
    if time_check(time.time(), tgrj_time):
        return
    else:
        tgrjtxt = await getdata('http://yanxi520.cn/api/tiangou.php')
        tgrj_time = time.time()
        await tgrj.finish(Message('%s' % tgrjtxt), at_sender=True)


xljt_time = 0


@xljt.handle()
async def _():
    global xljt_time
    if time_check(time.time(), xljt_time):
        return
    else:
        xjlttxt = await getdata('http://yanxi520.cn/api/xljtwr.php')
        xljt_time = time.time()
        await xljt.finish(Message('%s' % xjlttxt), at_sender=True)

#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/1 13:50
@author: 0xchang
@E-mail: oxchang@163.com
@file: upField.py
@Github: https://github.com/0xchang
"""
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Event
from bot2.plugins.xiuxian.Role import XianRole
from nonebot.adapters.onebot.v11.message import Message

upxian = on_fullmatch('进化', priority=239)


@upxian.handle()
async def infoxian_handle(event: GroupMessageEvent):
    uid = event.get_user_id()
    u = XianRole(uid, event.sender.nickname)
    if u.isBiguan():
        await upxian.finish(Message(f'你正在闭关'),at_sender=True)
    if u.goldToField():
        mess = '恭喜你消耗部分灵石进化成功，各项属性有所增加！'
    else:
        mess = '您的灵石不足'
    del u
    await upxian.finish(Message(mess))


jiujiupxian = on_fullmatch('大进化', priority=239)


@jiujiupxian.handle()
async def jiujiupxian_handle(event: Event):
    uid = event.get_user_id()
    u = XianRole(uid, event.sender.nickname)
    if u.biggoldToField():
        mess = '恭喜你消耗大量灵石进化100次，各项属性大量增加！'
    else:
        mess = '你的灵石不够了捏'
    await jiujiupxian.finish(Message(mess))


jiujiupxian = on_fullmatch('究极进化', priority=239)


@jiujiupxian.handle()
async def jiujiupxian_handle(event: Event):
    uid = event.get_user_id()
    u = XianRole(uid, event.sender.nickname)
    if u.supgoldToField():
        mess = '恭喜你消耗大量灵石进化10000次，各项属性大量增加！'
    else:
        mess = '你的灵石不够了捏'
    await jiujiupxian.finish(Message(mess))


btupxian = on_fullmatch('我是变态', priority=239)


@btupxian.handle()
async def btupxian_handle(event: Event):
    uid = event.get_user_id()
    u = XianRole(uid, event.sender.nickname)
    count = 0
    while u.supgoldToField() and count < 100:
        count += 1
    if count != 0:
        mess = f'恭喜你消耗大量灵石进化{count * 10000}次，各项属性大量增加！'
    else:
        mess = '你的灵石不够了捏'
    await btupxian.finish(Message(mess))

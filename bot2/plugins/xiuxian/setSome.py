#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/1 14:10
@author: 0xchang
@E-mail: oxchang@163.com
@file: setSome.py
@Github: https://github.com/0xchang
"""
from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from bot2.plugins.xiuxian.Role import XianRole
from nonebot.adapters.onebot.v11.message import Message
from nonebot.params import CommandArg

namexian = on_command('改名', priority=232)
@namexian.handle()
async def infoxian_handle(event: GroupMessageEvent,argcom:Message=CommandArg()):
    name=argcom.extract_plain_text()
    uid = event.get_user_id()
    u = XianRole(uid)
    u.setName(name)
    mess=f'改名成功，你的新名字为{name}'
    del u
    await namexian.finish(Message(mess))

sexxian = on_command('改性别', priority=237)
@sexxian.handle()
async def infoxian_handle(event: GroupMessageEvent,argcom:Message=CommandArg()):
    sex=argcom.extract_plain_text()
    uid = event.get_user_id()
    u = XianRole(uid)
    if sex=='男' or sex=='女' or sex=='阴阳人':
        u.setSex(sex)
        mess='你的性别改变成功'
    else:
        mess='改变性别失败，只能为男、女、阴阳人'
    del u
    await sexxian.finish(Message(mess))
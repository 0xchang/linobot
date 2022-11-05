#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/5 17:26
@author: 0xchang
@E-mail: oxchang@163.com
@file: colorname.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.params import CommandArg
from nonebot import on_command
from nonebot import get_bot

color_name = on_command('群昵称', priority=280)


@color_name.handle()
async def colorname_handle(event: GroupMessageEvent, argcom: Message = CommandArg()):
    bot = get_bot()
    #保留颜色符号，没有改成彩色名字
    color = ''
    print(event.get_plaintext())
    uid = event.get_user_id()
    gid = event.group_id
    argcom = argcom.extract_plain_text()
    argcom = argcom.strip()
    newname = color + argcom
    if len(newname.encode()) >= 60:
        await color_name.finish(Message('名字有点长了哦，短一点试试吧'))
    await bot.call_api('set_group_card',
                       group_id=gid,
                       user_id=uid,
                       card=newname)
    await color_name.finish(Message(f'成功改群名为{argcom}'))

#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/23 18:19
@author: 0xchang
@E-mail: oxchang@163.com
@file: fans.py
@Github: https://github.com/0xchang
"""
from bilibili_api import user
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from bot2.plugins.sql.select_sql import select_follow_group

fans=on_fullmatch('查粉')
@fans.handle()
async def fans_handle(event:GroupMessageEvent):
    values=select_follow_group('group',event.group_id)
    values=values.split('\n')
    mess=''
    for value in values:
        value=value.split(',')
        if len(value[0])==0:
            continue
        u = user.User(value[1])
        fol=await u.get_relation_info()
        fol=str(fol["follower"])
        mess+=value[0]+'的粉丝数为'+fol+'\n'
    mess=mess[:-1]
    await fans.finish(Message(mess))
#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/26 14:15
@author: 0xchang
@E-mail: oxchang@163.com
@file: wife.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot
from nonebot import on_command
import random

wife=on_command('抽老婆',priority=108)
@wife.handle()
async def wife_handle(bot:Bot,event:GroupMessageEvent):
    qqid=event.get_user_id()
    gid=event.group_id
    data=await bot.call_api('get_group_member_list',**{'group_id':gid})
    mywife=data[random.randint(0,len(data)-1)]
    mess=f'[CQ:at,qq={qqid}],您亲爱的老婆是[CQ:image,file=http://q.qlogo.cn/headimg_dl?dst_uin={mywife["user_id"]}&spec=140&img_type=jpg]【{mywife["nickname"]}】 ({mywife["user_id"]})呐!'
    await wife.finish(Message(mess))


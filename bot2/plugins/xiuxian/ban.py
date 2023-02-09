#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2023/1/29 1:40
@author: 0xchang
@E-mail: oxchang@163.com
@file: ban.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.params import CommandArg
from nonebot import on_command, Bot
from bot2.plugins.xiuxian.Role import XianRole
import random

ssyb = on_command('殊死一搏', priority=100, block=True)


@ssyb.handle()
async def ssyb_handle(bot: Bot, event: GroupMessageEvent, argcom: Message = CommandArg()):
    uid1 = event.get_user_id()
    uid2 = argcom[0].get('data').get('qq')
    gid = event.group_id
    u1 = XianRole(uid1)
    if u1.gold < 5000:
        await ssyb.finish(Message(f'你身上的灵石不够，要5k灵石'))
    u1.gold -= 5000
    del u1
    if random.randint(1,9)%2==0:
        die=uid1
    else:
        die=uid2
    await ssyb.send(Message(f'你花费了5k灵石和{uid2}进行对赌，输的一方将被禁言一分钟'))
    await ssyb.send(
        Message(f'刚才拼搏中招的人是{die}[CQ:image,file=http://q.qlogo.cn/headimg_dl?dst_uin={die}&spec=5&img_type=jpg]'))
    await bot.set_group_ban(group_id=gid, user_id=die, duration=60)
    await ssyb.finish(Message('他将被禁言一分钟'))

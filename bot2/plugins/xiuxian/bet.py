#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/12/2 23:27
@author: 0xchang
@E-mail: oxchang@163.com
@file: bet.py
@Github: https://github.com/0xchang
"""
import random

from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from bot2.plugins.xiuxian.Role import XianRole

betxian = on_command('赌灵石', priority=264)


@betxian.handle()
async def bet_handle(event: GroupMessageEvent, argcom: Message = CommandArg()):
    uid = event.get_user_id()
    flag = False
    arg = argcom.extract_plain_text().strip().split()
    if len(arg) != 2 or not arg[0].isdigit() or arg[1] not in ('单', '双', '大', '小'):
        await betxian.finish(Message('参数不对，应类似于 赌灵石 500 单/双/大/小'))
    magic = random.randint(1, 6)
    dgold = int(arg[0])
    dtype = arg[1]
    if dtype == '单' and magic % 2 == 1:
        flag = True
    elif dtype == '双' and magic % 2 == 0:
        flag = True
    elif dtype == '大' and magic > 3:
        flag = True
    elif dtype == '小' and magic < 4:
        flag = True
    u = XianRole(uid)
    if u.gold < dgold:
        del u
        await betxian.finish(Message('你身上的灵石不够了'), at_sender=True)
    else:
        mess = f'上天选中的数字是{magic},'
        if flag:
            mess += f'恭喜你,你赢了{dgold}灵石'
            u.gold += dgold
        else:
            mess += f'很遗憾,你输了{dgold}灵石'
            u.gold -= dgold
        del u
        await betxian.finish(Message(mess), at_sender=True)

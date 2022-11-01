#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/1 13:55
@author: 0xchang
@E-mail: oxchang@163.com
@file: morege.py
@Github: https://github.com/0xchang
"""
import random

from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from bot2.plugins.xiuxian.Role import XianRole
from nonebot.adapters.onebot.v11.message import Message

workxian = on_command('打工', priority=234)
@workxian.handle()
async def infoxian_handle(event: GroupMessageEvent):
    uid = event.get_user_id()
    u = XianRole(uid, event.sender.nickname)
    res=u.work()
    if res<=20:
        mess=f'你打工不认真，仅仅得了{res}灵石'
    elif res>=40:
        mess=f'你打工很认真，得了{res}灵石'
    else:
        mess=f'你打工一般，得了{res}灵石'
    del u
    await workxian.finish(Message(mess))

goods=['秋刀鱼','比目鱼','三文鱼','多宝鱼','石斑鱼','黑头鱼','马鲛','金目鲷','金枪鱼','军曹鱼']
bads=['破烂的鞋子','枯枝','烂木头','衣服','拖鞋','蛇']
fishxian = on_command('钓鱼', priority=235)
@fishxian.handle()
async def infoxian_handle(event: GroupMessageEvent):
    global goods
    global bads
    uid = event.get_user_id()
    u = XianRole(uid, event.sender.nickname)
    gold,exp=u.fishing()
    del u
    if gold+exp==0:
        mess='你没灵石买鱼饵了,快去打工吧！'
    elif gold+exp>10:
        mess=f'你钓鱼得到了{random.choice(goods)},灵石+{gold}，灵气+{exp}'
    else:
        mess=f'你钓鱼得到了{random.choice(bads)},灵石+{gold}，灵气+{exp}'
    await fishxian.finish(Message(mess))
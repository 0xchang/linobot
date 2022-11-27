#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/25 15:37
@author: 0xchang
@E-mail: oxchang@163.com
@file: welcome.py
@Github: https://github.com/0xchang
"""
from nonebot import on_notice
from nonebot.typing import T_State
from nonebot.adapters import Bot
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupIncreaseNoticeEvent

welcom = on_notice()

@welcom.handle()
async def welcome( event: GroupIncreaseNoticeEvent):
    user = event.get_user_id()
    at_ = "欢迎！：[CQ:at,qq={}]".format(user)
    msg = at_ + '加入大家庭,你可以使用/帮助来获取帮助信息'
    msg = Message(msg)
    await welcom.finish(message=Message(f'{msg}'))



#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/12/12 23:46
@author: 0xchang
@E-mail: oxchang@163.com
@file: yiqingsec.py
@Github: https://github.com/0xchang
"""
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11.message import Message
import os

yqsec=on_fullmatch('疫情安全',priority=326)
@yqsec.handle()
async def yqsec_handle():
    pwd = os.getcwd()
    path = os.path.join(pwd, 'img', 'yiqingsec.jpg')
    await yqsec.finish(Message(f'[CQ:image,file=file:///{path}]'))
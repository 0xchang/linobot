#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/30 21:44
@author: 0xchang
@E-mail: oxchang@163.com
@file: jingjiehelp.py.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_fullmatch

jingjiexian=on_fullmatch('境界帮助')
@jingjiexian.handle()
async def jingjie_handle():
    await jingjiexian.finish(Message('练气期、筑基期、结丹期、金丹期、元婴期、出窍期、化神期、渡劫期、天仙、真仙、玄仙、金仙、仙君、仙尊、仙帝、神人、真神、大神、天神、金神、玄神、古神、神王、神君、神尊、神帝、鸿钧'))
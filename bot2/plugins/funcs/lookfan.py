#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/2 12:31
@author: 0xchang
@E-mail: oxchang@163.com
@file: lookfan.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_command
from nonebot.params import CommandArg
from urllib.parse import quote

fancmd=on_command('看番',priority=270)
@fancmd.handle()
async def songer_handle(argcom:Message=CommandArg()):
    word=argcom.extract_plain_text()
    wordurl='https://www.agemys.net/search?query='+quote(word)+'&page=1'
    mess=wordurl
    await fancmd.finish(Message(mess))
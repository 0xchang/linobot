#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/12/31 21:21
@author: 0xchang
@E-mail: oxchang@163.com
@file: r18.py
@Github: https://github.com/0xchang
"""
import time

from nonebot import on_fullmatch
import requests
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Bot
import json
import asyncio

r18 = on_fullmatch('r18')



@r18.handle()
async def r18handle(bot: Bot):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    imgurl = requests.get(url='https://moe.jitsu.top/r18/', headers=headers, allow_redirects=False).headers[
        'Location']
    print(imgurl)
    mid = (await r18.send(Message(f'[CQ:image,file={imgurl}]')))['message_id']
    await asyncio.sleep(7)
    await bot.delete_msg(message_id=mid)


pr18 = on_fullmatch('pr18')


@pr18.handle()
async def pr18handle(bot: Bot):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    text = requests.get(url='https://moe.jitsu.top/img/?sort=r18&type=json', headers=headers).text
    data = json.loads(text)
    imgurl = data['pics'][0]
    mid = (await pr18.send(Message(f'[CQ:image,file={imgurl}]')))['message_id']
    await asyncio.sleep(7)
    await bot.delete_msg(message_id=mid)

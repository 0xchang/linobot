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
import urllib.parse

from nonebot import on_fullmatch, on_startswith
import requests
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
import json
import asyncio

r18 = on_fullmatch({'r18', 'R18'}, priority=330, block=False)


@r18.handle()
async def r18handle(bot: Bot):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    imgurl = requests.get(url='https://moe.anosu.top/r18/', headers=headers, allow_redirects=False).headers[
        'Location']
    time.sleep(0.7)
    mid = (await pr18.send(Message(f'图片太se发不出来，给你网址自己看吧\n{imgurl}')))['message_id']
    await asyncio.sleep(30)
    await bot.delete_msg(message_id=mid)


pr18 = on_fullmatch({'pr18', 'PR18', 'Pr18'}, priority=330, block=False)


@pr18.handle()
async def pr18handle(bot: Bot):
    flag = False
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    text = requests.get(url='https://moe.anosu.top/img/?sort=r18&type=json', headers=headers).text
    data = json.loads(text)
    imgurl = data['pics'][0]
    time.sleep(0.7)
    try:
        mid = (await pr18.send(Message(f'[CQ:image,file={imgurl}]')))['message_id']
        nmid = (await pr18.send(Message(f'图片原网址,不清晰可转移\n{imgurl}')))['message_id']
        flag = True
    except:
        mid = (await pr18.send(Message(f'图片太se发不出来，给你网址自己看吧\n{imgurl}')))['message_id']
    await asyncio.sleep(30)
    if flag:
        await bot.delete_msg(message_id=nmid)
    await bot.delete_msg(message_id=mid)


seci = on_startswith({'涩词', 'seci', '塞词'}, priority=330, block=False)


@seci.handle()
async def _seci(bot: Bot, event: GroupMessageEvent):
    flag = False
    arg = event.get_plaintext().split()[1]
    arg = urllib.parse.urlencode({'keyword': arg})
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    resp = requests.get(f'https://image.anosu.top/pixiv/json?{arg}', headers=headers).text
    resp = json.loads(resp)
    imgurl = resp[0]['url']
    try:
        mid = (await pr18.send(Message(f'[CQ:image,file={imgurl}]')))['message_id']
        nmid = (await pr18.send(Message(f'图片原网址,不清晰可转移\n{imgurl}')))['message_id']
        flag = True
    except:
        mid = (await pr18.send(Message(f'图片太se发不出来，给你网址自己看吧\n{imgurl}')))['message_id']
    await asyncio.sleep(30)
    if flag:
        await bot.delete_msg(message_id=nmid)
    await bot.delete_msg(message_id=mid)

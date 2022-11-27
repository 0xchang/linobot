#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/25 19:07
@author: 0xchang
@E-mail: oxchang@163.com
@file: getelement.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_command
from nonebot.params import CommandArg
import requests
import json
from PIL import Image, ImageDraw, ImageFont
import os

getele=on_command('查成分',priority=292)
@getele.handle()
async def getele_handle(argcom:Message=CommandArg()):
    uid=argcom.extract_plain_text()
    uid=uid.strip()
    if not uid.isdigit():
        await getele.finish(Message('UID必须为纯数字'))
    url=f'https://api.danmaku.suki.club/api/search/user/channel?uid={uid}'
    resp=requests.get(url).text
    dic=json.loads(resp)
    if dic['code']!=200:
        await getele.finish(Message(f'可能没查到'))
    data=dic['data']
    res=set()
    for d in data:
        res.add(d['name'])
    mess=f'ta的关注数为{len(res)}\n'
    count=0
    for r in res:
        if count%2==0:
            mess+=r+' '*50
        else:
            mess+=r+'\n'
        count+=1
    mess=mess[:-1]
    txt2Image(mess)
    path = os.path.join(os.getcwd(), 'img', 'chengfen.png')
    await getele.finish(Message(f'[CQ:image,file=file:///{path}]'))

def txt2Image(txt:str):
    lino_path = os.path.join(os.getcwd(), 'img', 'lino.jpg')
    current = Image.open(lino_path)
    draw = ImageDraw.Draw(current)
    font = ImageFont.truetype(os.path.join(os.getcwd(), 'fonts', 'qiantuxiaotuti.ttf'), size=36)
    draw.text((20, 420), text=txt, font=font, fill=(94, 38, 18))
    current.save('./img/chengfen.png')

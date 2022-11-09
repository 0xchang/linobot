#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/11/9 13:01
@author: 0xchang
@E-mail: oxchang@163.com
@file: randgirl.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_fullmatch
import requests

rand_pic = on_fullmatch('随机壁纸', priority=190)

rand_pic.handle()


@rand_pic.handle()
async def rand_pic_handle():
    res = requests.get('http://api.iw233.cn/api.php?sort=random', allow_redirects=False)
    await rand_pic.finish(Message(f'[CQ:image,file={res.headers["Location"]}]'))


rand_girl = on_fullmatch('随机美女', priority=190)

rand_girl.handle()


@rand_girl.handle()
async def rand_girl_handle():
    res = requests.get('http://api.iw233.cn/api.php?sort=iw233', allow_redirects=False)
    await rand_girl.finish(Message(f'[CQ:image,file={res.headers["Location"]}]'))


top_pic = on_fullmatch('壁纸推荐', priority=190)

top_pic.handle()


@top_pic.handle()
async def top_pic_handle():
    res = requests.get('http://api.iw233.cn/api.php?sort=random', allow_redirects=False)
    await top_pic.finish(Message(f'[CQ:image,file={res.headers["Location"]}]'))


white_girl = on_fullmatch('银发少女', priority=190)

white_girl.handle()


@white_girl.handle()
async def white_girl_handle():
    res = requests.get('http://ap1.iw233.cn/api.php?sort=yin', allow_redirects=False)
    await white_girl.finish(Message(f'[CQ:image,file={res.headers["Location"]}]'))


catear_pic = on_fullmatch('兽耳少女', priority=190)

catear_pic.handle()


@catear_pic.handle()
async def catear_pic_handle():
    res = requests.get('http://ap1.iw233.cn/api.php?sort=cat', allow_redirects=False)
    await catear_pic.finish(Message(f'[CQ:image,file={res.headers["Location"]}]'))


mp_pic = on_fullmatch('竖屏少女', priority=190)

mp_pic.handle()


@mp_pic.handle()
async def mp_pic_handle():
    res = requests.get('http://api.iw233.cn/api.php?sort=mp', allow_redirects=False)
    await mp_pic.finish(Message(f'[CQ:image,file={res.headers["Location"]}]'))

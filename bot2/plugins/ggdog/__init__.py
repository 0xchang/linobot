#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2023/4/30 23:46
@author: 0xchang
@E-mail: oxchang@163.com
@file: __init__.py
@Github: https://github.com/0xchang
"""
# 使用狗哥api相关操作
from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_fullmatch
import aiohttp

gghelp = on_fullmatch('狗哥帮助')
ggqq = on_fullmatch('求签')
ggjkzf = on_fullmatch('JK制服')
ggsjdmt = on_fullmatch('随机动漫图')
ggxjjsp = on_fullmatch('小姐姐视频')
ggsjmt = on_fullmatch('随机美腿')


@gghelp.handle()
async def _():
    helpmess = '''
    ***狗哥帮助***
求签--求个签子试试
JK制服--可能是好看的吧
随机动漫图--看看
小姐姐视频--流鼻血了吗
随机美腿--好看不
来自狗哥api'''
    await gghelp.finish(helpmess)


@ggsjmt.handle()
async def _():
    url = await get('http://www.ggapi.cn/api/legs', 'location')
    await ggsjdmt.finish(Message('[CQ:image,file={}]'.format(url)))


@ggxjjsp.handle()
async def _():
    url = await get('http://www.ggapi.cn/api/jkzf', 'location')
    await ggxjjsp.finish(Message('[CQ:video,file={}]'.format(url)))


@ggsjdmt.handle()
async def _():
    url = await get('http://www.ggapi.cn/api/acg?type=url')
    await ggsjdmt.finish(Message('[CQ:image,file={}]'.format(url)))


@ggjkzf.handle()
async def _():
    url = await get('http://www.ggapi.cn/api/jkzf', 'location')
    await ggjkzf.finish(Message('[CQ:image,file={}]'.format(url)))


@ggqq.handle()
async def _():
    content = await get('http://www.ggapi.cn/api/qiuqian')
    await ggqq.finish(content, at_sender=True)


async def get(url, content: str = 'body'):
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=5)) as se:
        async with se.get(url) as g:
            if content == 'body':
                r = await g.text()
            elif content == 'location':
                r = g.history[0].headers.get('Location')
            elif content == 'json':
                r = await g.json()
    return r

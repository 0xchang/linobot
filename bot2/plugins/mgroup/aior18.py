#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2023/2/16 15:27
@author: 0xchang
@E-mail: oxchang@163.com
@file: aior18.py
@Github: https://github.com/0xchang
"""
import json

import aiohttp


async def getdata(url) -> dict:
    async with aiohttp.ClientSession(headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
            , requote_redirect_url=False, timeout=aiohttp.ClientTimeout(2)) as session:
        resp = await session.get(url)
        data = await resp.text()
        data = json.loads(data)
    return data

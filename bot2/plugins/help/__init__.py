#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/15 11:36
@author: 0xchang
@E-mail: oxchang@163.com
@file: __init__.py
@Github: https://github.com/0xchang
"""
from nonebot import on_command

allhelp = on_command('帮助', aliases={'菜单'}, priority=90)


@allhelp.handle()
async def _():
    helpmenu = '''帮助
b战帮助
吃饭帮助
群帮助
老婆帮助
言溪帮助
修仙帮助
插件帮助'''
    await allhelp.finish(helpmenu)

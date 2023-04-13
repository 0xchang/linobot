#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2023/2/15 16:55
@author: 0xchang
@E-mail: oxchang@163.com
@file: __init__.py
@Github: https://github.com/0xchang
"""

import os
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot
from nonebot import on_command, on_fullmatch, on_regex
from nonebot.params import CommandArg
import random
from .wifedbs import WifesDB, WifeDBSet
from nonebot import require

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler

if not os.path.exists('data'):
    os.mkdir('data')

WifesDB.create()

newwife = on_regex('^[抽换]老婆$', priority=110)
enwife = on_regex('^[解禁]老婆$', priority=110)
stealwife = on_command('偷老婆', priority=110)
helpwife = on_fullmatch('老婆帮助', priority=110)
cwife = on_fullmatch('c老婆', priority=110)
mwife = on_fullmatch('摸老婆', priority=110)


@mwife.handle()
async def _(event: GroupMessageEvent):
    gid = event.group_id
    uid = event.get_user_id()
    if WifeDBSet.sel_gid(gid):
        res = WifesDB.sel_gau(gid, uid)
        if res:
            res = res[0]
            await mwife.finish(Message(
                f'你轻轻地摸了一下你的老婆[CQ:image,file=http://q.qlogo.cn/headimg_dl?dst_uin={res[2]}&spec=5&img_type=jpg]{res[3]}更喜欢你了'))
        else:
            await mwife.finish('你还没有老婆，去抽一个吧')
    else:
        await mwife.finish('未开启老婆功能')


@cwife.handle()
async def _(event: GroupMessageEvent):
    gid = event.group_id
    uid = event.get_user_id()
    if WifeDBSet.sel_gid(gid):
        res = WifesDB.sel_gau(gid, uid)
        if res:
            res = res[0]
            await cwife.finish(Message(
                f'你狠狠地c了一顿你的老婆[CQ:image,file=http://q.qlogo.cn/headimg_dl?dst_uin={res[2]}&spec=5&img_type=jpg]{res[3]}欲罢不能了'))
        else:
            await cwife.finish('你还没有老婆，去抽一个吧')
    else:
        await cwife.finish('未开启老婆功能')


@enwife.handle()
async def _(event: GroupMessageEvent):
    gid = event.group_id
    text = event.get_plaintext()
    if '解' in text:
        WifeDBSet.update(gid, True)
    else:
        WifeDBSet.update(gid, False)
    await enwife.finish(text + '成功')


@newwife.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    gid = event.group_id
    uid = int(event.get_user_id())
    text = event.get_plaintext()
    WifeDBSet.insert(gid)
    if WifeDBSet.sel_gid(gid):
        res = WifesDB.sel_gau(gid, uid)
        if '抽' in text and res:
            res = res[0]
            await newwife.finish(
                Message(
                    f'您亲爱的老婆是[CQ:image,file=http://q.qlogo.cn/headimg_dl?dst_uin={res[2]}&spec=5&img_type=jpg]【{res[3]}】 ({res[2]})呐!'))
        else:
            data = await bot.call_api('get_group_member_list', group_id=gid)
            mywife = random.choice(data)
            mess = f',您亲爱的老婆是[CQ:image,file=http://q.qlogo.cn/headimg_dl?dst_uin={mywife["user_id"]}&spec=5&img_type=jpg]【{mywife["nickname"]}】 ({mywife["user_id"]})呐!'
            WifesDB.insert(gid, uid, mywife['user_id'], mywife['nickname'])
            WifesDB.update(gid, uid, mywife['user_id'], mywife['nickname'])
            await newwife.finish(Message(mess))
    else:
        await newwife.finish('未开启老婆功能')


@stealwife.handle()
async def _(event: GroupMessageEvent, argcom: Message = CommandArg()):
    uid = argcom[0].get('data').get('qq')
    gid = event.group_id
    value = WifesDB.sel_gau(gid, uid)
    if not value:
        await stealwife.finish('他连老婆都没有呢，你看他这么可怜别偷了！')
    value=value[0]
    if random.randint(1, 4) == 1:
        wid = value[2]
        name = value[3]
        WifesDB.update(gid, int(event.get_user_id()), wid, name)
        await stealwife.finish('恭喜你偷到了老婆，快看看你老婆吧!', at_sender=True)
    await stealwife.finish('你偷老婆失败了，等会再来吧')


@scheduler.scheduled_job("cron", hour=3, minute=0)
async def clean_wife():
    WifesDB.clear()


@helpwife.handle()
async def _():
    helpmenu = '''
    ***老婆帮助***
禁老婆--不允许抽老婆
解老婆--可以了
抽老婆--展示你的老婆
换老婆--换一个老婆
偷老婆--偷别人的老婆
c老婆--emmm
摸老婆--摸一下你的老婆'''
    await helpwife.finish(helpmenu)

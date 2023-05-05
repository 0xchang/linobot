#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/14 23:35
@author: 0xchang
@E-mail: oxchang@163.com
@file: __init__.py
@Github: https://github.com/0xchang
"""
import asyncio
import os, time
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot import on_command, on_fullmatch, on_regex
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER
from bilibili_api import user, live
from nonebot.adapters.onebot.v11 import GROUP_ADMIN, GROUP_OWNER
from nonebot import require
from nonebot import get_bots

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
from .bilidbs import BiliDB, UpDB, UpGroupDB, GroupDB
from .video_ti_q import vmess
from .updynamic import dyn
from .uplive import uplive
from .live2q import live_bye
from .bilihelp import create_bilihelp_img
import json
import requests

from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="b站插件",
    description="这是一个b站vup帮助插件",
    usage="",
    extra={},
)

# 创建文件夹
if not os.path.exists('data'):
    os.mkdir('data')

BiliDB.create_table()
create_bilihelp_img()

get_follow = on_command('关注列表', priority=80, block=True)
follow_info = on_command('关注设置', priority=80, block=True)
# 与petpet插件冲突，提高优先级
follow = on_command('关注', priority=4, permission=SUPERUSER | GROUP_OWNER | GROUP_ADMIN, block=True)
nofollow = on_command('取关', priority=81, permission=SUPERUSER | GROUP_OWNER | GROUP_ADMIN, block=True)
dahanghai = on_fullmatch('查舰', priority=82, block=True)
fans = on_fullmatch('查粉', priority=82, block=True)
dyn_vi_li_open = on_regex('^(开启|关闭)(全体)?(动态|视频|直播)$', priority=82, permission=SUPERUSER | GROUP_OWNER | GROUP_ADMIN,
                          block=True)
vcmd = on_command('投稿', priority=83, block=True)
topd = on_fullmatch('置顶', priority=83)
last = on_fullmatch('最新', priority=83)
bilimenu = on_command('b站帮助', aliases={'b站菜单'}, priority=84)


@follow.handle()
async def _(event: GroupMessageEvent, comargs: Message = CommandArg()):
    '''获取关注主播space数字并存入bili.db'''
    # 哔哩哔哩查看主播是否存在API,使用bilibili-api进行访问
    uid = comargs.extract_plain_text()
    if uid.isdigit():
        # b站api有更新，频繁访问会导致json解析错误，改为其他api
        url = f'https://api.bilibili.com/x/space/wbi/acc/info?mid={uid}&token=&platform=web'
        info = requests.get(url, timeout=2, headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'})
        info = json.loads(info.text).get('data')
        uid = info.get('mid')
        name = info.get('name')
        live_room = info.get('live_room')
        if live_room is None:
            await follow.finish('这个up没有自己的直播间，所以不关注了')
        rid = live_room.get('roomid')
        gid = event.group_id
        UpDB.insert(uid, rid, name)
        GroupDB.insert(gid)
        UpGroupDB.insert(uid, gid)
        await follow.finish(f'已关注{name}({uid})了哦', at_sender=True)
    else:
        await follow.finish('你输入的主播id有误,您可以重来吗?谢谢!', at_sender=True)


@dahanghai.handle()
async def _(event: GroupMessageEvent):
    gid = event.group_id
    uids = UpGroupDB.sel_gid(gid)
    if not uids:
        return
    for uid in uids:
        uid = uid[0]
        up = UpDB.sel_uid(uid)[0]
        rid = up[1]
        name = up[2]
        r = live.LiveRoom(rid)
        resp = await r.get_dahanghai()
        num = resp['info']['num']
        time.sleep(0.2)
        await dahanghai.send(f'{name}目前已经拥有《{num}》舰长啦 这是大家对lino的喜欢捏 大步向前继续努力吧喵！')


@dyn_vi_li_open.handle()
async def _(event: GroupMessageEvent):
    gid = event.group_id
    mess = event.get_plaintext()
    flag1 = 1 if '开启' in mess else 0
    flag2 = '全体' in mess
    if '动态' in mess:
        if flag2:
            GroupDB.update_dynat(gid, flag1)
        else:
            GroupDB.update_dyn(gid, flag1)
    elif '视频' in mess:
        if flag2:
            GroupDB.update_videoat(gid, flag1)
        else:
            GroupDB.update_video(gid, flag1)
    elif '直播' in mess:
        if flag2:
            GroupDB.update_liveat(gid, flag1)
        else:
            GroupDB.update_live(gid, flag1)
    await dyn_vi_li_open.finish(f'已经{"开启" if flag1 else "关闭"}{"全体" if flag2 else ""}{mess[-2:]}通知')


@fans.handle()
async def _(event: GroupMessageEvent):
    gid = event.group_id
    uids = UpGroupDB.sel_gid(gid)
    if not uids:
        return
    for uid in uids:
        uid = uid[0]
        up = UpDB.sel_uid(uid)[0]
        u = user.User(up[0])
        name = up[2]
        fol = await u.get_relation_info()
        fol = str(fol["follower"])
        mess = name + '的粉丝数有' + fol + '个哦,谢谢支持喵!'
        time.sleep(0.2)
        await fans.send(mess)


@get_follow.handle()
async def _(event: GroupMessageEvent):
    gid = event.group_id
    uids = UpGroupDB.sel_gid(gid)
    if not uids:
        await get_follow.finish('该群没有关注任何主播')
    mess = ''
    for uid in uids:
        uid = uid[0]
        res = UpDB.sel_uid(uid)[0]
        name = res[2]
        mess += f'{name}|{uid}\n'
    await get_follow.finish(f'该群关注列表为\n{mess}')


@nofollow.handle()
async def _(event: GroupMessageEvent, comargs: Message = CommandArg()):
    uid = comargs.extract_plain_text()
    if not uid.isdigit():
        await nofollow.finish(f'uid必须为纯数字')
    gid = event.group_id
    uid = int(uid)
    BiliDB.delete(uid, gid)
    await nofollow.finish(f'{uid}已取关')


@follow_info.handle()
async def _(event: GroupMessageEvent):
    gid = event.group_id
    res = GroupDB.sel_gid(gid)
    if not res:
        await follow_info.finish('该群没有关注任何人')
    r = res[0]
    rdict = {
        '直播': True if r[1] else False,
        '动态': True if r[2] else False,
        '视频': True if r[3] else False,
        '全体直播': True if r[4] else False,
        '全体动态': True if r[5] else False,
        '全体视频': True if r[6] else False,
    }
    mess = json.dumps(rdict, ensure_ascii=False)
    await follow_info.finish(f'该群关注设置为\n' + mess)


@vcmd.handle()
async def _(event: GroupMessageEvent, argcom: Message = CommandArg()):
    gid = event.group_id
    argcom = argcom.extract_plain_text()
    uids = UpGroupDB.sel_gid(gid)
    if not uids:
        await vcmd.finish('该群没有关注任何主播')
    for uid in uids:
        mess = await vmess(uid[0], argcom)
        await vcmd.send(Message(mess))


@topd.handle()
async def _(event: GroupMessageEvent):
    gid = event.group_id
    uids = UpGroupDB.sel_gid(gid)
    for uid in uids:
        uid = uid[0]
        infos = UpDB.sel_uid(uid)[0]
        res = await dyn(uid, infos[2], True)
        res = res[2]
        mess = res
        mess = mess.replace('发布了新', '的置顶')
        await topd.send(Message(mess))


@last.handle()
async def _(event: GroupMessageEvent):
    gid = event.group_id
    uids = UpGroupDB.sel_gid(gid)
    for uid in uids:
        uid = uid[0]
        infos = UpDB.sel_uid(uid)[0]
        res = await dyn(uid, infos[2], False)
        res = res[2]
        mess = res
        mess = mess.replace('发布了新', '的置顶')
        await last.send(Message(mess))

@scheduler.scheduled_job("cron", second='*/15')
async def while_live():
    bot, = get_bots().values()
    ups = UpDB.sel()
    if not ups:
        return
    for up in ups:
        mess, pnum, startTime = await uplive(up[1], up[2])
        gids = UpGroupDB.sel_uid(up[0])
        if startTime != 0 and up[4] == 0:
            for gid in gids:
                time.sleep(0.1)
                gid = gid[1]
                groupSet = GroupDB.sel_gid(gid)[0]
                if groupSet[1] != 0:
                    if groupSet[4] == 0:
                        send = mess
                    else:
                        send = '[CQ:at,qq=all]' + mess

                    await bot.send_msg(
                        message_type='group',
                        group_id=gid,
                        message=send,
                    )
                    # 发送消息更新数据库
                    UpDB.update_send(up[0], 1)
        elif startTime == 0 and up[4] == 1:
            mess = live_bye(up[2], pnum, up[3])
            for gid in gids:
                time.sleep(0.1)
                gid = gid[1]
                groupSet = GroupDB.sel_gid(gid)[0]
                if groupSet[1] != 0:
                    await bot.send_msg(
                        message_type='group',
                        group_id=gid,
                        message=mess,
                    )
                    UpDB.update_send(up[0], 0)
                    # 设置间隔0.2秒
                    await asyncio.sleep(0.2)


@scheduler.scheduled_job("cron", second='*/20')
async def while_dyn():
    bot, = get_bots().values()
    ups = UpDB.sel()
    if not ups:
        return
    for up in ups:
        now = time.time()
        rtype, sendtime, mess = await dyn(up[0], up[2], False)
        if now - sendtime > 21:
            continue
        gids = UpGroupDB.sel_uid(up[0])
        for gid in gids:
            gid = gid[1]
            groupSet = GroupDB.sel_gid(gid)
            groupSet = groupSet[0]
            if groupSet[2] == groupSet[3] == 0:
                continue
            send = mess
            # 当类型为视频且视频at开，或全体动态开则+at all
            if (rtype == 8 and groupSet[6] == 1) or (groupSet[5] == 1):
                send = '[CQ:at,qq=all]' + mess
            await bot.send_msg(
                message_type='group',
                group_id=gid,
                message=send,
            )
            #设置发消息间隔0.2秒
            await asyncio.sleep(0.2)


@bilimenu.handle()
async def _():
    helpinfo = '''
    ***b站菜单***
关注uid--关注主播
取关uid--取关主播
关注列表--查看关注了哪些主播
关注设置--看群关注的设置
(开启/关闭)(全体)(直播/动态/视频)--对群进行设置
置顶--查看up动态置顶信息
最新--查看最新动态
投稿--查看up投稿视频，默认0
查粉--看看粉丝有多少
查舰--看看你有多少个亲爱的舰长'''
    await bilimenu.finish(helpinfo)

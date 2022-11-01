#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/15 21:10
@author: 0xchang
@E-mail: oxchang@163.com
@file: follow.py
@Github: https://github.com/0xchang
"""
'''
关注主播id,暂设权限仅支持SUPERUSER
'''
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Event
from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER
from bilibili_api import user
from bot2.plugins.sql import insert_sql,select_sql,del_sql
from nonebot.adapters.onebot.v11 import GROUP_ADMIN, GROUP_OWNER

follow=on_command('关注',priority=4,permission=SUPERUSER|GROUP_OWNER|GROUP_ADMIN)
@follow.handle()
async def follow_handle(event:Event,comargs:Message=CommandArg()):
    '''获取关注主播space数字并存入data.sqlite'''
    #哔哩哔哩查看主播是否存在API,使用bilibili-api进行访问
    uid=comargs.extract_plain_text()
    if uid.isdigit():
        uid=int(uid)
        u=user.User(uid)
        info=await u.get_user_info()
        mid=info['mid']
        name=info['name']
        live_room=info['live_room']
        roomid=live_room['roomid']
        #获取到字符串事件type字符串
        alltype=event.message_type
        if alltype=='private':
            qid=event.user_id
        if alltype=='group':
            qid=event.group_id
        #创建user/fgroup表,同步
        #查询表中数据,uid是否存在,存在则返回已关注,同步
        res_user=select_sql.select_user(mid)
        res_group=select_sql.select_group(mid,alltype,qid)
        res_live=select_sql.select_live(mid)
        #user表中的数据,没有则添加
        if len(res_user)==0:
            insert_sql.insert_user(mid,name,roomid)
        if len(res_live) == 0:
            insert_sql.insert_live(mid,0)
        #group表中数据,没有则添加
        if len(res_group)!=0:
            await follow.finish(Message(f'[CQ:at,qq={event.get_user_id()}]您已经关注了%s哦'%res_user[0][1]))
        else:
            insert_sql.insert_group(mid,roomid,alltype,qid)
            await follow.finish(Message(f'[CQ:at,qq={event.get_user_id()}]已关注%s(%d)了哦'%(name,mid)))
    else:
        await follow.finish(Message(f'[CQ:at,qq={event.get_user_id()}]你输入的主播id有误,您可以重来吗?谢谢!'))

get_follow=on_command('关注列表',priority=151)
@get_follow.handle()
async def get_follow_handle(event:Event):
    if event.message_type=='group':
        qid=event.group_id
    if event.message_type=='private':
        qid=event.user_id
    res=select_sql.select_follow_group(event.message_type,qid)
    if len(res)==0:
        await get_follow.finish(Message(f'[CQ:at,qq={event.get_user_id()}]没有关注任何人'))
    await get_follow.finish(Message(f'[CQ:at,qq={event.get_user_id()}]关注列表为\n%s'%res))

nofollow=on_command('取关',priority=152,permission=SUPERUSER)
#操作取关事件
@nofollow.handle()
async def nofollow_handle(event:Event,comargs:Message=CommandArg()):
    uid=comargs.extract_plain_text()
    if not uid.isdigit():
        await nofollow.finish(Message(f'uid必须为纯数字'))
    else:
        if event.message_type=='private':
            qid=event.user_id
        if event.message_type=='group':
            qid=event.group_id
        uid=int(uid)
        res=select_sql.select_group(uid,event.message_type,qid)
        if not len(res)!=0:
            await nofollow.finish(Message(f'没有关注%d'%uid))
        else:
            name = select_sql.select_user(uid)[0][1]
            del_sql.del_group(uid,event.message_type,qid)
            del_sql.del_user(uid)
            await nofollow.finish(Message(f'%s已取关'%name))

follow_info=on_command('关注详情',priority=156)
@follow_info.handle()
async def follow_info_handle(event:Event):
    if event.message_type=='group':
        qid=event.group_id
    if event.message_type=='private':
        qid=event.user_id
    res=select_sql.select_follow_info(event.message_type,qid)
    if len(res)==0:
        await get_follow.finish(Message(f'[CQ:at,qq={event.get_user_id()}]没有关注任何人'))
    await get_follow.finish(Message(f'[CQ:at,qq={event.get_user_id()}]关注列表为\n%s'%str(res)))
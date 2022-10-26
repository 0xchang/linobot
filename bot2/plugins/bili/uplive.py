#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/18 14:06
@author: 0xchang
@E-mail: oxchang@163.com
@file: uplive.py
@Github: https://github.com/0xchang
"""
from bilibili_api import live
from bot2.plugins.sql.update_sql import update_data,update_live_sta

async def uplive(roomid:int,name:str):
    r=live.LiveRoom(roomid)
    liveres=await r.get_room_info()
    pnum=liveres['watched_show']['num']
    liveres=liveres['room_info']
    uid=liveres['uid']
    liveUrl='https://live.bilibili.com/'+str(roomid)
    title=liveres['title']
    cover=liveres['cover']
    stime=liveres['live_start_time']
    res=name+'开播了,快去看看喵\n'+title+'\n[CQ:image,file=%s]\n'%cover+liveUrl
    #print(res)
    status=1
    if stime==0:
        status=0
    else:
        update_data(update_live_sta(uid,status,stime))
    return (stime,res,(uid,name,status,pnum,stime))
#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/18 9:49
@author: 0xchang
@E-mail: oxchang@163.com
@file: updynamic.py
@Github: https://github.com/0xchang
"""
#获取up动态信息并进行解析
from bilibili_api import user
import bot2.plugins.sql as sql

async def dyn(uid:int)->(int,int,str):
    name=sql.select_sql.select_user(uid)[0][1]
    u=user.User(uid)
    res=await u.get_dynamics()
    contype=res['cards'][0]['desc']['type']
    mess = '%s发布了新动态,大家快去瞅瞅\n'%name
    if contype==1:
        return (contype,0,mess)
    elif contype==2:
        desccripton=res['cards'][0]['card']['item']['description']
        mess+=desccripton+'\n'
        for pic in res['cards'][0]['card']['item']['pictures']:
            pic=pic['img_src']
            mess+=f'[CQ:image,file=%s]'%pic
    elif contype==4:
        mess+=res['cards'][0]['card']['item']['content']
    elif contype==8:
        mess+=res['cards'][0]['card']['title']
        mess+='[CQ:image,file:%s]'%res['cards'][0]['card']['pic']
        mess+='这是一条视频哦!快去看喵!%s'%res['cards'][0]['card']['short_link']
        return (contype,res['cards'][0]['desc']['timestamp'],mess)
    mess+='\nhttps://t.bilibili.com/'+str(res['cards'][0]['desc']['dynamic_id'])
    return (contype,res['cards'][0]['desc']['timestamp'],mess)
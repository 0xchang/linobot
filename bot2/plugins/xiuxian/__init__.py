#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/31 20:53
@author: 0xchang
@E-mail: oxchang@163.com
@file: __init__.py
@Github: https://github.com/0xchang
"""
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot import on_fullmatch
from .Role import xian_db, Player, Attribute, Exp, Race
from peewee import ModelSelect
import time,json

def init_data():
    race=json.load(open('race_init.json','r'))
    Race.insert_many(race).on_conflict_replace().execute()


init_data()

start = on_fullmatch('进入修仙世界', priority=200)
death = on_fullmatch('重生', priority=200)


@start.handle()
async def _(event: GroupMessageEvent):
    # 初始化数据，姓名无名氏，种族随机,性别随机
    uid = event.get_user_id()
    xian_db.connect()
    player: ModelSelect = Player.select().where(Player.id == uid)
    if player:
        xian_db.close()
        await start.finish('你早已进入了修仙世界,如果感觉活不下去,使用<重生>来逆天改命')
    else:
        Player.create(id=uid, gender='男', name=event.sender.nickname, create_at=time.time(), status=0)
        Attribute.create(player=player, hp=100, mp=50,
                         hp_max=100, mp_max=50, phy_attack=20,
                         phy_defense=20, mag_attack=20,
                         mag_defense=20, attack_speed=0,
                         moving_speed=3600, hit_rate=5, evade=3,
                         gold=100)
        Exp.create(player=player)
        xian_db.close()
        await start.finish('恭喜你已进入修仙世界,请使用<修仙帮助/修仙查询>获取信息吧')


@death.handle()
async def _(event: GroupMessageEvent):
    uid = event.get_user_id()
    xian_db.connect()
    player: ModelSelect = Player.select().where(Player.id == uid)
    if player:
        # 清除数据,先删exp等副属性,最后删player
        Exp.delete().where(Exp.player == player).execute()
        Player.delete().where(Player.id == uid).execute()
        xian_db.close()
        await death.finish('没想到你选择重生,走好不送')
    else:
        xian_db.close()
        await death.finish('你已经选择重生了，请输入<进入修仙世界>重活一世吧')

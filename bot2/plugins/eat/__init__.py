#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2023/2/13 17:08
@author: 0xchang
@E-mail: oxchang@163.com
@file: __init__.py
@Github: https://github.com/0xchang
"""
from nonebot import require

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
from nonebot import get_bots
import os
import random

from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_regex, on_fullmatch

if not os.path.exists('img'):
    os.mkdir('img')

if not os.path.exists('img/eat'):
    os.mkdir('img/eat')

if not os.path.exists('data'):
    os.mkdir('data')

if not os.path.exists('data/eat.txt'):
    # 创建空文件
    with open('data/eat.txt', 'w') as f:
        pass
eathelp = on_fullmatch('吃饭帮助', priority=150)
eatcmd = on_regex('^([早午晚]饭|水果)$', priority=150)
eatremcmd = on_regex('^(开启|关闭)吃饭服务$', priority=150)


@eathelp.handle()
async def _():
    ehelp = '''
    ***吃饭帮助***
早饭--看看早上吃什么
午饭--看看中午吃什么
晚饭--看看晚上吃什么
水果--看看吃什么水果
(开启/关闭)吃饭服务--每天三问'''
    await eathelp.finish(ehelp)


@eatremcmd.handle()
async def _(event: GroupMessageEvent):
    gid = str(event.group_id) + '\n'
    with open('data/eat.txt', 'r') as f:
        li = f.readlines()
    if '开启' in event.get_plaintext():
        if not gid in li:
            with open('data/eat.txt', 'w') as f:
                f.write(gid)
                f.writelines(li)
    else:
        if gid in li:
            with open('data/eat.txt', 'w') as f:
                for l in li:
                    if gid != l:
                        f.write(l)
    await eatcmd.finish('已' + event.get_plaintext())


@eatcmd.handle()
async def _(event: GroupMessageEvent):
    getmess = event.get_plaintext()
    breakfast = ('煎饼果子', '水煎包', '皮蛋瘦肉粥', '咸鸭粥', '胡辣汤', '炸糖糕', '炸菜角', '鸡蛋灌饼', '灌汤包', '咸豆腐脑', '菜盒',
                 '油馍头', '肉夹馍', '烧麦', '豆浆油条', '土豆饼', '锅贴', '馄饨', '肠粉', '羊杂汤', '鱿鱼仔', '秘制咸鸭蛋',
                 '香菇鲜肉包', '涪陵榨菜')
    lunch = ('咸烧白', '可乐鸡翅', '京酱肉丝', '梅菜扣肉', '锅包肉', '馄饨', '鱼香肉丝', '毛血旺', '烤鸭',
             '番茄炒蛋', '糖醋里脊', '红烧肉', '红烧排骨', '粉蒸排骨', '粉蒸牛肉', '清蒸鱼', '白灼生菜', '小鸡炖蘑菇',
             '小葱拌豆腐', '红烧鸡翅', '清炖羊肉', '清炒西兰花', '香菇肉片', '猪肚炖鸡', '蒜末炒肉', '蒜蓉炒油麦菜', '腊肉炒豆角',
             '酱焖黄花鱼', '红烧鸡肉', '辣炒肥肠', '清蒸大虾', '豆角炒肉', '白菜炖豆腐', '烧饼', '鸭锁骨', '虾条', '黑芝麻球')
    dinner = ('咸烧白', '可乐鸡翅', '京酱肉丝', '梅菜扣肉', '锅包肉', '馄饨', '鱼香肉丝', '毛血旺', '烤鸭',
              '番茄炒蛋', '糖醋里脊', '红烧肉', '红烧排骨', '粉蒸排骨', '粉蒸牛肉', '清蒸鱼', '白灼生菜', '小鸡炖蘑菇',
              '小葱拌豆腐', '红烧鸡翅', '清炖羊肉', '清炒西兰花', '香菇肉片', '猪肚炖鸡', '蒜末炒肉', '蒜蓉炒油麦菜', '腊肉炒豆角',
              '酱焖黄花鱼', '红烧鸡肉', '辣炒肥肠', '清蒸大虾', '豆角炒肉', '白菜炖豆腐', '烧饼', '鸭锁骨', '虾条', '黑芝麻球')
    fruits = ('苹果', '梨', '葡萄', '红提', '枣', '柑橘', '桃', '西瓜', '杏', '甜瓜', '香瓜', '荔枝', '甘蔗',
              '柿', '柠檬', '香蕉', '芒果', '菠萝', '哈密瓜', '李子', '石榴', '枸杞', '山楂', '椰子', '桑葚',
              '柚子', '草莓', '沙糖桔', '木瓜', '橙', '圣女果', '龙眼', '黄瓜', '枇杷', '山竹', '红毛丹', '无花果',
              '杨桃', '人参果', '猕猴桃', '芭乐', '杨梅', '乌梅', '蓝莓', '西梅', '释迦', '百花果', '黄皮',
              '樱桃', '雪莲果', '榴莲', '火龙果', '番石榴', '菠萝蜜', '百香果', '罗汉果', '莲雾', '核桃', '板栗',
              '开心果', '榛子', '银杏', '松子', '果仁', '白果', '果脯', '槟榔果', '腰果', '果汁',
              '果酒', '罐头', '果酱', '果干', '脱水水果', '果茶')
    if '早' in getmess:
        eating = random.sample(breakfast, 3)
    elif '午' in getmess:
        eating = random.sample(lunch, 3)
    elif '晚' in getmess:
        eating = random.sample(dinner, 3)
    else:
        eating = random.sample(fruits, 3)
    eat = '、'.join(eating)
    path = os.path.join(os.getcwd(), "img", "eat", "{}.jpg")
    mess = '你现在是想吃' + eat + '吗[CQ:face,id=66]' + ''.join(
        [f'[CQ:image,file=file:///{path.format(e)}]' for e in eating if os.path.exists(path.format(e))])
    await eatcmd.finish(Message(mess))


# 催早饭
@scheduler.scheduled_job("cron", hour=8, minute=30)
async def good_morning():
    bot, = get_bots().values()
    with open('data/eat.txt', 'r') as f:
        gids = f.readlines()
    for gid in gids:
        gid = int(gid)
        await bot.send_msg(
            message_type="group",
            group_id=gid,
            message='亲爱的小宝贝，你吃早饭了吗[CQ:face,id=12]'
        )


# 催午饭
@scheduler.scheduled_job("cron", hour=12, minute=10)
async def good_afternoon():
    bot, = get_bots().values()
    with open('data/eat.txt', 'r') as f:
        gids = f.readlines()
    for gid in gids:
        gid = int(gid)
        await bot.send_msg(
            message_type="group",
            group_id=gid,
            message='亲爱的大宝贝，你吃午饭了吗[CQ:face,id=24]'
        )


# 催晚饭
@scheduler.scheduled_job("cron", hour=17, minute=30)
async def good_night():
    bot, = get_bots().values()
    with open('data/eat.txt', 'r') as f:
        gids = f.readlines()
    for gid in gids:
        gid = int(gid)
        await bot.send_msg(
            message_type="group",
            group_id=gid,
            message='亲爱的宝贝，你吃晚饭了吗[CQ:face,id=21]'
        )

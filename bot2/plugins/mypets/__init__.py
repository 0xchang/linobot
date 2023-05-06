#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2023/5/7 0:07
@author: 0xchang
@E-mail: oxchang@163.com
@file: __init__.py
@Github: https://github.com/0xchang
"""

from nonebot.params import CommandArg
from nonebot import on_command, on_fullmatch
from .petdbs import Pets, petlive, petupexp
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot import require
import time

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler

Pets.create_table()

petstype = {'哈士奇', '柴犬', '阿拉斯加', '萨摩耶', '金毛', '英短', '美短', '中华田园猫', '波斯猫', '银狐仓鼠', '紫仓', '三线仓鼠', '普色密袋鼬',
            '白色密袋鼬', '铂金密袋鼬', '豹纹守宫', '睫角守宫', '鬃狮蜥', '刺猬', '玄凤鹦鹉', '虎皮鹦鹉', '牡丹鹦鹉', '米色', '丝绒黑龙猫',
            '金色龙猫', '标准灰龙猫', '苏利羊驼', '华卡约羊驼', '金鱼', '蝴蝶鱼', '孔雀鱼', '牦牛', '水牛', '黄牛', '西伯利亚虎',
            '华南虎', '印度支那虎', '马来亚虎', '垂耳兔', '侏儒兔', '荷兰兔', '海棠兔', '乌梢蛇', '马', '呼伦贝尔羊', '波尔山羊',
            '鬼狒狒', '杏花鸡', '火鸡', '家猪', '野猪', '喜鹊', '乌鸦', '孔雀', '橘猫', '企鹅', '海豹', '海豚', '狮子', '大象'}

petstart = on_command('领养宠物', priority=105)
pethelp = on_fullmatch('宠物帮助', priority=105)
petend = on_fullmatch('放生宠物', priority=105)
petstatus = on_fullmatch('宠物状态', priority=105)
petsign = on_fullmatch('宠物签到', priority=105)
petrevive = on_fullmatch('宠物复活', priority=105)
petall = on_fullmatch('宠物种类', priority=105)
petname = on_command('宠物取名', priority=105)
peteat = on_fullmatch('给宠物喂食', priority=105)
petdrink = on_fullmatch('给宠物喝水', priority=105)
petplay = on_fullmatch('陪宠物玩耍', priority=105)
petstudy = on_fullmatch('让宠物学习', priority=105)

studystatus = dict()


@peteat.handle()
async def _(event: GroupMessageEvent):
    uid = event.get_user_id()
    pet: Pets = Pets.get_or_none(Pets.uid == uid)
    if pet:
        if petlive(pet):
            if pet.coins < 5:
                await peteat.finish('你的金币不够，快去签到吧')
            else:
                pet.coins -= 5
                pet.hunger += 20
                if pet.hunger > 100:
                    pet.hunger = 100
                petupexp(pet, 3)
                pet.save()
                await peteat.finish(f'你喂食了{pet.name}，经验+3，{pet.name}肚子大了一点点')
        else:
            await peteat.finish('你的宠物好像不行了，快复活你的宠物吧')
    else:
        await peteat.finish('你还没有宠物快去领养吧')


@petdrink.handle()
async def _(event: GroupMessageEvent):
    uid = event.get_user_id()
    pet: Pets = Pets.get_or_none(Pets.uid == uid)
    if pet:
        if petlive(pet):
            if pet.coins < 5:
                await petdrink.finish('你的金币不够，快去签到吧')
            else:
                pet.coins -= 5
                pet.thirst += 20
                if pet.thirst > 100:
                    pet.thirst = 100
                petupexp(pet, 2)
                pet.save()
                await petdrink.finish(f'你给{pet.name}喝水了，经验+2，{pet.name}肚子大了一点点')
        else:
            await petdrink.finish('你的宠物好像不行了，快复活你的宠物吧')
    else:
        await petdrink.finish('你还没有宠物快去领养吧')


@petplay.handle()
async def _(event: GroupMessageEvent):
    uid = event.get_user_id()
    pet: Pets = Pets.get_or_none(Pets.uid == uid)
    if pet:
        if petlive(pet):
            if pet.happiness >= 96:
                await petplay.finish('你的宠物非常开心，不需要玩耍了')
            pet.happiness += 5
            petupexp(pet, 1)
            pet.save()
            await petplay.finish(f'你陪{pet.name}玩耍了，经验+1，{pet.name}更开心了')
        else:
            await petplay.finish('你的宠物好像不行了，快复活你的宠物吧')
    else:
        await petplay.finish('你还没有宠物快去领养吧')


@petstudy.handle()
async def _(event: GroupMessageEvent):
    uid = event.get_user_id()
    pet: Pets = Pets.get_or_none(Pets.uid == uid)
    if pet:
        if petlive(pet):
            if not studystatus.get(uid):
                studystatus[uid] = time.time()
            else:
                if time.time() - studystatus.get(uid) < 1800:
                    await petstudy.finish(f'你刚教完{pet.name}学习完，等会再来吧')
            petupexp(pet, 6)
            pet.save()
            await petstudy.finish(f'你教{pet.name}学了一些指令，经验+6，{pet.name}更聪明了')
        else:
            await petstudy.finish('你的宠物好像不行了，快复活你的宠物吧')
    else:
        await petstudy.finish('你还没有宠物快去领养吧')


@petrevive.handle()
async def _(event: GroupMessageEvent):
    uid = event.get_user_id()
    pet: Pets = Pets.get_or_none(Pets.uid == uid)
    if pet:
        if pet.coins < 50:
            await petrevive.finish('你身上的金币不够,宠物无法复活,需要50金币')
        if petlive(pet):
            await petrevive.finish('宠物还活着，不需要复活')
        pet.coins -= 50
        pet.hunger = 50
        pet.thirst = 50
        pet.happiness = 50
        pet.save()
        await petrevive.finish('你的宠物已经复活')
    else:
        await petrevive.finish('你还没有宠物快去领养吧')


@petall.handle()
async def _():
    await petall.finish(','.join(petstype))


@petname.handle()
async def _(event: GroupMessageEvent, arg: Message = CommandArg()):
    uid = event.get_user_id()
    name = arg.extract_plain_text().strip()
    pet: Pets = Pets.get_or_none(Pets.uid == uid)
    if pet:
        pet.name = name
        pet.save()
        await petname.finish(f'你的宠物已更名为{name}')
    else:
        await petname.finish('你还没有宠物快去领养吧')


@petstatus.handle()
async def _(event: GroupMessageEvent):
    uid = event.get_user_id()
    pet: Pets = Pets.get_or_none(Pets.uid == uid)
    if pet:
        await petstatus.finish("""宠物名字:{}
宠物种类:{}
金币   :{}
宠物饥饿:{}
宠物口渴:{}
宠物欢乐:{}
宠物经验:{}
宠物等级:{}""".format(pet.name, pet.pet_type, pet.coins, pet.hunger, pet.thirst, pet.happiness, pet.exp, pet.level))
    else:
        await petstatus.finish('你还没有宠物快去领养吧')


@petsign.handle()
async def _(event: GroupMessageEvent):
    uid = event.get_user_id()
    pet: Pets = Pets.get_or_none(Pets.uid == uid)
    if pet:
        pet.coins += 60
        petupexp(pet,5)
        pet.save()
        await petsign.finish('恭喜您签到获取60金币,宠物经验+5')
    else:
        await petsign.finish('你还没有宠物快去领养吧')


@petstart.handle()
async def _(event: GroupMessageEvent, arg: Message = CommandArg()):
    ptype = arg.extract_plain_text().strip()
    if not ptype in petstype:
        await petstart.finish('您要领养的宠物较为稀有，我们暂未收录')
    uid = event.get_user_id()
    pet: Pets = Pets.get_or_none(Pets.uid == uid)
    if pet:
        await petstart.finish(f'你已领养宠物{pet.pet_type}')
    else:
        Pets.create(uid=uid,
                    name="未取名",
                    pet_type=ptype,
                    coins=100,
                    hunger=100,
                    thirst=100,
                    happiness=100,
                    exp=0,
                    level=1
                    )
        await petstart.finish(f'您已领养宠物{ptype},快点取名吧,记住一个人只能领养一个宠物哦!')


@petend.handle()
async def _(event: GroupMessageEvent):
    uid = event.get_user_id()
    pet: Pets = Pets.get_or_none(Pets.uid == uid)
    if pet:
        pet.delete()
        await petend.finish('你已放生了你的宠物，它再也不会回来了。')
    else:
        await petend.finish('你还没有宠物快去领养吧')


@scheduler.scheduled_job("cron", hour='*/1')
async def while_pet2consume():
    Pets.update(hunger=Pets.hunger - 3).where(Pets.hunger >= 0).execute()
    Pets.update(thirst=Pets.thirst - 3).where(Pets.thirst >= 0).execute()
    Pets.update(happiness=Pets.happiness - 1).where(Pets.happiness >= 0).execute()


@pethelp.handle()
async def _():
    peth = '''    ***宠物帮助***
领养宠物 xx--领养你自己的宠物，一个人只有一个
放生宠物--不要抛弃宠物好吗
宠物状态--查看宠物状态
宠物签到--签到得金币
宠物复活--复活你的宠物
宠物种类--看看有哪些类型的宠物
宠物取名 xx--给宠物取名
给宠物喂食--给宠物喂吃的
给宠物喝水--给宠物喝水
陪宠物玩耍--陪宠物玩耍
让宠物学习--教宠物一些指令/间隔半小时'''
    await pethelp.finish(peth)

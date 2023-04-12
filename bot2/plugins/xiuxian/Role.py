#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2023/3/11 8:46
@author: 0xchang
@E-mail: oxchang@163.com
@file: Role.py
@Github: https://github.com/0xchang
"""
import time

from peewee import Model, SqliteDatabase, IntegerField, TextField, CharField, ForeignKeyField, FloatField, ModelSelect, \
    PrimaryKeyField

xian_db = SqliteDatabase('../../../data/xian.db')


# 玩家
class Player(Model):
    id = IntegerField(unique=True, primary_key=True)
    name = CharField(max_length=18, default='无名氏')
    gender = CharField(max_length=1, default='男')
    # 状态
    # 0 空闲,-1 死亡,1 打怪,2 打工,3 钓鱼
    status = IntegerField(default=0)
    create_at = FloatField()

    class Meta:
        database = xian_db


# 属性
class Attribute(Model):
    player = ForeignKeyField(Player, backref='attributes', unique=True)
    hp = IntegerField()
    mp = IntegerField()
    hp_max = IntegerField()
    mp_max = IntegerField()
    phy_attack = IntegerField()
    phy_defense = IntegerField()
    mag_attack = IntegerField()
    mag_defense = IntegerField()
    attack_speed = IntegerField()
    moving_speed = IntegerField()
    hit_rate = IntegerField()
    evade = IntegerField()
    gold = IntegerField()

    class Meta:
        database = xian_db


# 经验
class Exp(Model):
    player = ForeignKeyField(Player, backref='exp', unique=True)
    player_level = IntegerField(default=0)
    player_exp = IntegerField(default=0)
    player_exp_max = IntegerField(default=200)
    alchemy_level = IntegerField(default=0)
    alchemy_exp = IntegerField(default=0)
    alchemy_exp_max = IntegerField(default=20)
    refiner_level = IntegerField(default=0)
    refiner_exp = IntegerField(default=0)
    refiner_exp_max = IntegerField(default=50)

    class Meta:
        database = xian_db


# 种族
class Race(Model):
    id = IntegerField(unique=True)
    name = CharField(max_length=5)
    description = TextField()
    # 属性加成
    phy_at_up = FloatField()
    phy_de_up = FloatField()
    mag_at_up = FloatField()
    mag_de_up = FloatField()
    at_sp_up = FloatField()
    mov_sp_up = FloatField()
    hit_up = FloatField()
    evade_up = FloatField()

    class Meta:
        database = xian_db


# 背包
class Backpack(Model):
    id = PrimaryKeyField()
    player = ForeignKeyField(Player)
    item_id = IntegerField()
    quantity = IntegerField()

    class Meta:
        database = xian_db


# 丹药
class Drug(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=10)
    grade = CharField(max_length=5)
    # 血量，蓝量，经验值
    effect = CharField(max_length=25)
    # 数量
    amount = IntegerField()
    description = TextField()
    # 材料(如 紫兰草 回春花 西风果)
    materials = CharField(max_length=50)
    # 炼丹所需时间
    time_required = IntegerField()

    class Meta:
        database = xian_db


# 进化石
class Evolve(Model):
    id = IntegerField(unique=True)
    name = CharField(max_length=10)
    grade = CharField(max_length=1)
    level = IntegerField()
    # +物理攻击+物理防御+法术攻击
    # +法术防御+攻速+移速+命中率+闪避
    effect = CharField(max_length=30)
    amount = IntegerField()
    description = TextField()

    class Meta:
        database = xian_db


# 药草
class Herbs(Model):
    id = IntegerField(unique=True)
    name = CharField(max_length=10, unique=True)
    description = TextField()

    class Meta:
        database = xian_db


# 矿石
class Ore(Model):
    id = IntegerField(unique=True)
    name = CharField(max_length=10, unique=True)
    description = TextField()

    class Meta:
        database = xian_db


# 武器
class Weapon(Model):
    id = IntegerField(unique=True)
    name = CharField(max_length=20, unique=True)
    # 材料
    materials = CharField(max_length=50)
    description = TextField()
    effect = CharField(max_length=30)
    amount = IntegerField()
    multiple = FloatField()

    class Meta:
        database = xian_db


# 商店
class Shop(Model):
    commodity_id = IntegerField(unique=True)
    purchasing_price = IntegerField()
    selling_price = IntegerField()

    class Meta:
        database = xian_db


# 技能
class Skill(Model):
    id = IntegerField(unique=True)
    name = CharField(max_length=20)
    effect = IntegerField()
    amount = IntegerField()
    multiple = FloatField()
    level = IntegerField()
    description = TextField()

    class Meta:
        database = xian_db


# 功法,仅增加经验值*倍数
class Cultivation(Model):
    id = IntegerField(unique=True)
    multiple = FloatField()
    description = TextField()

    class Meta:
        database = xian_db


# 怪物
class Monster(Model):
    id = IntegerField(unique=True)
    description = TextField()
    # 状态 1存活 0死亡
    status = IntegerField()
    hp = IntegerField()
    mp = IntegerField()
    phy_attack = IntegerField()
    phy_defense = IntegerField()
    mag_attack = IntegerField()
    mag_defense = IntegerField()
    attack_speed = IntegerField()
    hit_rate = IntegerField()
    evade = IntegerField()
    gold = IntegerField()
    drop = CharField(max_length=20)
    drop_probability = FloatField()

    class Meta:
        database = xian_db


# Boss
class Boss(Model):
    id = IntegerField(unique=True)
    description = TextField()
    # 状态 1存活 0死亡
    status = IntegerField()
    hp = IntegerField()
    mp = IntegerField()
    phy_attack = IntegerField()
    phy_defense = IntegerField()
    mag_attack = IntegerField()
    mag_defense = IntegerField()
    attack_speed = IntegerField()
    hit_rate = IntegerField()
    evade = IntegerField()
    gold = IntegerField()
    drop = CharField(max_length=100)
    drop_probability = FloatField()

    class Meta:
        database = xian_db


if __name__ == '__main__':
    xian_db.connect()
    xian_db.create_tables(
        [Player, Attribute, Exp, Race, Backpack, Drug, Evolve, Herbs, Ore, Weapon, Shop, Skill, Cultivation, Monster,
         Boss])
    player1: ModelSelect = Player.select().where(Player.id == 1)
    if player1:
        # 如果存在退出
        print(player1.dicts())
    else:
        # 不存在创建
        Player.create(id=1, gender='女', name='test1', create_at=time.time(), status=0)
        Attribute.create(player=player1, hp=50, mp=20,
                         hp_max=50, mp_max=20, phy_attack=20,
                         phy_defense=20, mag_attack=20,
                         mag_defense=20, attack_speed=3,
                         moving_speed=4, hit_rate=13, evade=13,
                         gold=121)
        Exp.create(player=player1)
    # 初始化种族数据
    race = [
        {'id': 1, 'name': '人',
         'description': '普通而平凡的人类。虽然没有像其他种族那样天生拥有特殊的能力，但是可以通过修炼和培养来获得更强大的力量和技能。',
         'phy_at_up': 1.5, 'phy_de_up': 1.5, 'mag_at_up': 1, 'mag_de_up': 1, 'at_sp_up': 1.1, 'mov_sp_up': 1,
         'hit_up': 1.1, 'evade_up': 1.1},
        {'id': 2, 'name': '鬼',
         'description': '邪恶和恐怖的存在。他们的修炼方法通常是通过吸取人类灵魂或者使用黑暗魔法来获得力量，与佛和人类相对立。',
         'phy_at_up': 1.1, 'phy_de_up': 1.2, 'mag_at_up': 1.5, 'mag_de_up': 0.8, 'at_sp_up': 1.1, 'mov_sp_up': 1,
         'hit_up': 1, 'evade_up': 1.5},
        {'id': 3, 'name': '妖',
         'description': '一种常见的种族。他们通常有强大的魔法能力，可以操纵元素、变身和吸取其他生物的灵魂能量。',
         'phy_at_up': 0.8, 'phy_de_up': 1.2, 'mag_at_up': 1.5, 'mag_de_up': 1.5, 'at_sp_up': 1, 'mov_sp_up': 1,
         'hit_up': 1.1, 'evade_up': 1},
        {'id': 4, 'name': '魔',
         'description': '邪恶和险恶的种族。修炼邪门歪道，比如吸取其他生物的精气或者使用禁忌魔法。被其他种族视为敌对势力。',
         'phy_at_up': 0.8, 'phy_de_up': 1.1, 'mag_at_up': 1.5, 'mag_de_up': 1.1, 'at_sp_up': 1.5, 'mov_sp_up': 1,
         'hit_up': 1.3, 'evade_up': 1},
        {'id': 5, 'name': '仙',
         'description': '飘逸和神秘的存在。通过修炼来提高自己的力量和境界，可以操控天地之力和飞行穿梭于不同的空间。',
         'phy_at_up': 1.5, 'phy_de_up': 1.2, 'mag_at_up': 0.7, 'mag_de_up': 1.2, 'at_sp_up': 1.1, 'mov_sp_up': 1,
         'hit_up': 1, 'evade_up': 1.5},
        {'id': 6, 'name': '佛',
         'description': '慈悲和正义的种族。通过修行和超脱来提高自己的精神境界和力量。是正义力量，与魔相对立。',
         'phy_at_up': 1.2, 'phy_de_up': 1.5, 'mag_at_up': 0.8, 'mag_de_up': 1.5, 'at_sp_up': 1, 'mov_sp_up': 1,
         'hit_up': 1, 'evade_up': 1},
        {'id': 7, 'name': '神',
         'description': '强大而神秘的存在，掌管着自然和人类的命运。力量和影响力超出其他种族的想象，但是他们往往不会干预人类的世界。',
         'phy_at_up': 1.6, 'phy_de_up': 1.6, 'mag_at_up': 1.1, 'mag_de_up': 1.1, 'at_sp_up': 1.2, 'mov_sp_up': 1,
         'hit_up': 1.1, 'evade_up': 1},
    ]
    Race.insert_many(race).on_conflict_replace().execute()
    drug = [
        {'id': 1, 'name': '回血丹', 'grade': '完美', 'effect': 'hp', 'amount': 100,
         'description': '可以回复血量',
         'materials': '回甘草 紫兰草 清风草', 'time_required': 5},
        {'id': 2, 'name': '回血丹', 'grade': '极品', 'effect': 'hp', 'amount': 80,
         'description': '描述',
         'materials': '回甘草 紫兰草 清风草', 'time_required': 5},
        {'id': 3, 'name': '回血丹', 'grade': '普通', 'effect': 'hp', 'amount': 60,
         'description': '描述',
         'materials': '回甘草 紫兰草 清风草', 'time_required': 5},
        {'id': 4, 'name': '回血丹', 'grade': '劣质', 'effect': 'hp', 'amount': 40,
         'description': '描述',
         'materials': '回甘草 紫兰草 清风草', 'time_required': 5},
        {'id': 5, 'name': '回蓝丹', 'grade': '完美', 'effect': 'hp', 'amount': 100,
         'description': '可以回复血量',
         'materials': '回甘草 紫兰草 清风草', 'time_required': 5},
        {'id': 6, 'name': '回蓝丹', 'grade': '极品', 'effect': 'hp', 'amount': 80,
         'description': '描述',
         'materials': '回甘草 紫兰草 清风草', 'time_required': 5},
        {'id': 7, 'name': '回蓝丹', 'grade': '普通', 'effect': 'hp', 'amount': 60,
         'description': '描述',
         'materials': '回甘草 紫兰草 清风草', 'time_required': 5},
        {'id': 8, 'name': '回蓝丹', 'grade': '劣质', 'effect': 'hp', 'amount': 40,
         'description': '描述',
         'materials': '回甘草 紫兰草 清风草', 'time_required': 5},
        {'id': 9, 'name': '经验丹', 'grade': '完美', 'effect': 'hp', 'amount': 100,
         'description': '可以回复血量',
         'materials': '回甘草 紫兰草 清风草', 'time_required': 5},
        {'id': 10, 'name': '经验丹', 'grade': '极品', 'effect': 'hp', 'amount': 80,
         'description': '描述',
         'materials': '回甘草 紫兰草 清风草', 'time_required': 5},
        {'id': 11, 'name': '经验丹', 'grade': '普通', 'effect': 'hp', 'amount': 60,
         'description': '描述',
         'materials': '回甘草 紫兰草 清风草', 'time_required': 5},
        {'id': 12, 'name': '经验丹', 'grade': '劣质', 'effect': 'hp', 'amount': 40,
         'description': '描述',
         'materials': '回甘草 紫兰草 清风草', 'time_required': 5},
    ]
    Drug.insert_many(drug).on_conflict_replace().execute()
    # Player.delete().execute()
    # Attribute.delete().execute()
    # Exp.delete().execute()
    xian_db.close()

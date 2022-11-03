#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2022/10/31 20:53
@author: 0xchang
@E-mail: oxchang@163.com
@file: Role.py
@Github: https://github.com/0xchang
"""
import random
import sqlite3
import time
from bot2.plugins.xiuxian.AMonster import Monster, MonBoss


class XianRole:
    def __init__(self, uid: int, name: str = '无名氏', sex: str = '男'):
        self.uid = uid
        self.name = name
        self.gold = 0
        self.attack = 20
        self.defense = 10
        self.speed = 6
        self.HP = 100
        self.MP = 50
        self.level = 1
        self.experience = 0
        self.stime = int(time.time())
        self.sex = sex
        self.signStatus = 0
        self.killnum = 0
        self.fishnum = 0
        self.dazuonum = 0
        self.worknum = 0
        self.getSql()

    def clear(self):
        self.gold = 0
        self.attack = 20
        self.defense = 10
        self.speed = 6
        self.HP = 100
        self.MP = 50
        self.level = 1
        self.experience = 0
        self.stime = int(time.time())
        self.signStatus = 0
        self.killnum = 0
        self.fishnum = 0
        self.dazuonum = 0
        self.worknum = 0
        self.upSql()

    def biguan(self, bt: int):
        con = sqlite3.connect('data/xiuxian.data')
        cur = con.cursor()
        cur.execute('select * from biguan where uid=?', (self.uid,))
        con.commit()
        va = cur.fetchall()
        if len(va) == 0:
            cur.execute('insert into biguan(uid,xtime,jtime) values(?,?,?)', (self.uid, int(time.time()), bt))
            con.commit()
            self.experience += 30 * bt
            now = int(time.time())
        else:
            jt = va[0][2]
            va = va[0][1]
            if int(time.time()) - va > jt * 60:
                cur.execute('update biguan set xtime=?,jtime=? where uid=?', (int(time.time()), bt, self.uid))
                con.commit()
                self.experience += 30 * bt
                now = int(time.time())
            else:
                now = int(time.time()) - va
        print(now, va)
        cur.close()
        con.close()
        return now

    def isBiguan(self):
        con = sqlite3.connect('data/xiuxian.data')
        cur = con.cursor()
        cur.execute('select * from biguan where uid=?', (self.uid,))
        con.commit()
        va = cur.fetchall()
        cur.close()
        con.close()
        if len(va) == 0:
            return False
        else:
            jt = va[0][2]
            xt = va[0][1]
            if int(time.time()) - xt > jt * 60:
                return False
            else:
                return True

    def setSex(self, sex: str):
        self.sex = sex

    def getGold(self):
        return self.gold

    def setGold(self, gold: int):
        self.gold = gold

    def setName(self, name: str):
        self.name = name

    def getName(self):
        return self.name

    def upHPMP(self) -> bool:
        if self.gold < 20:
            return False
        else:
            self.gold -= 20
            self.MP += 30
            self.HP += 50
            return True

    def upBigHPMP(self):
        if self.gold < 200:
            return False
        else:
            self.gold -= 200
            self.MP += 330
            self.HP += 530
            return True

    def upSuperHPMP(self):
        if self.gold < 2000:
            return False
        else:
            self.gold -= 2000
            self.MP += 3800
            self.HP += 5800
            return True

    def kmonboss(self, m: MonBoss) -> (bool, int, int, int):
        count = 0
        at1 = self.attack - m.getDefense()
        at2 = m.getAttack() - self.defense
        at1 = 0 if at1 <= 0 else at1 * 3
        at2 = 0 if at2 <= 0 else at2 * 3
        if at1 == 0 and at2 == 0:
            return False, 0, 0
        while m.getHP() > 0 and self.HP > 0:
            self.MP -= 2
            count += 1
            m.HP -= at1
            self.HP -= at2
        if m.getHP() > 0:
            return False, 0, 0, 0
        else:
            zgold = (m.getAttack() + m.getDefense()) * count // 2
            zexp = zgold * 4
            self.gold += zgold
            self.experience += zexp
            con = sqlite3.connect('data/xiuxian.data')
            cur = con.cursor()
            cur.execute('update monboss set live=? where name=?', (0, m.name))
            con.commit()
            cur.close()
            con.close()
            return True, zgold, zexp, at2

    def kmonster(self, m: Monster) -> (bool, int, int):
        count = 0
        at1 = self.attack - m.getDefense()
        at2 = m.getAttack() - self.defense
        at1 = 0 if at1 <= 0 else at1 * 3
        at2 = 0 if at2 <= 0 else at2 * 3
        if at1 == 0 and at2 == 0:
            return False, 0, 0
        while m.getHP() > 0 and self.HP > 0:
            self.MP -= 2
            count += 1
            m.HP -= at1
            self.HP -= at2
        if m.getHP() > 0:
            return False, 0, 0
        else:
            zgold = (m.getAttack() + m.getDefense()) * count // 10
            self.gold += zgold
            return True, zgold, at2

    def kten(self, u1) -> str:
        for i in range(10):
            self.kill(u1)
        return '你攻击了十次'

    def kill(self, u1) -> str:
        if self.MP <= 0:
            return '你的蓝量不足，不能攻击'
        if self.HP <= 0:
            self.gold -= 15
            return f'你的血量为0,你掉了一些15灵石'
        self.MP -= 2
        u1.MP -= 2
        self.killnum += 1
        if u1.HP <= 0:
            u1.gold -= 25
            self.gold += 25
            return '你要攻击的人的血量为0,你捡起来了他的25灵石'
        if self.speed >= u1.speed:
            # 先攻击
            at1 = self.attack - u1.defense
            at2 = u1.attack - self.defense
            at1 = 0 if at1 <= 0 else at1 * 5
            at2 = 0 if at2 <= 0 else at2 * 5
            u1.HP -= at1
            if u1.HP > 0:
                self.HP -= at2
                if self.HP > 0:
                    return f'回合结束！你掉了{at2}血，他掉了{at1}血'
                self.gold -= 25
                u1.gold += 25
                return '你死了，他捡起了你的25灵石'
            u1.gold -= 25
            self.gold += 25
            return '他死了，你捡起了他的25灵石'
        else:
            # 后攻击
            at1 = u1.attack - self.defense
            at1 = 0 if at1 <= 0 else at1 * 5
            at2 = self.attack - u1.defense
            at2 = 0 if at2 <= 0 else at2 * 5
            self.HP -= at1
            if self.HP > 0:
                u1.HP -= at2
                if u1.HP > 0:
                    return f'回合结束！你掉了{at1}血，他掉了{at2}血'
                self.gold += 25
                u1.gold -= 25
                return '他死了，你捡起了他的25灵石'
            u1.gold += 25
            self.gold -= 25
            return '你死了，他捡起了你的25灵石'

    def xianlevel(self) -> str:
        level = self.level
        n0 = level // 10
        n1 = level % 10
        honor = ''
        if n0 < 1:
            honor += '练气期'
        elif n0 < 2:
            honor += '筑基期'
        elif n0 < 3:
            honor += '结丹期'
        elif n0 < 4:
            honor += '金丹期'
        elif n0 < 5:
            honor += '元婴期'
        elif n0 < 6:
            honor += '出窍期'
        elif n0 < 7:
            honor += '化神期'
        elif n0 < 8:
            honor += '渡劫期'
        elif n0 < 9:
            honor += '天仙'
        elif n0 < 10:
            honor += '真仙'
        elif n0 < 11:
            honor += '玄仙'
        elif n0 < 12:
            honor += '金仙'
        elif n0 < 13:
            honor += '仙君'
        elif n0 < 14:
            honor += '仙尊'
        elif n0 < 15:
            honor += '仙帝'
        elif n0 < 16:
            honor += '神人'
        elif n0 < 17:
            honor += '真神'
        elif n0 < 18:
            honor += '大神'
        elif n0 < 19:
            honor += '天神'
        elif n0 < 20:
            honor += '金神'
        elif n0 < 21:
            honor += '玄神'
        elif n0 < 22:
            honor += '古神'
        elif n0 < 23:
            honor += '神王'
        elif n0 < 24:
            honor += '神君'
        elif n0 < 25:
            honor += '神尊'
        elif n0 < 26:
            honor += '神帝'
        else:
            honor += '鸿钧'
        honor += f'{num_to_char(n1)}阶'
        if '鸿钧' in honor:
            honor = '鸿钧'
        return honor

    def honor(self):
        honor = self.killhonor() + ',' + self.dazuohonor() + ',' + self.workhonor() + ',' + self.fishhonor()
        return honor

    def workhonor(self) -> str:
        work = self.worknum
        if work < 100:
            honor = '打工新人'
        elif work < 500:
            honor = '打工油条'
        elif work < 1000:
            honor = '打工狂魔'
        else:
            honor = '打工肝帝'
        return honor

    def fishhonor(self) -> str:
        fish = self.fishnum
        if fish < 100:
            hornor = '钓鱼新手'
        elif fish < 500:
            hornor = '钓鱼油条'
        elif fish < 1000:
            hornor = '钓鱼狂魔'
        else:
            hornor = '钓鱼肝帝'
        return hornor

    def dazuohonor(self) -> str:
        dazuo = self.dazuonum
        if dazuo < 100:
            honor = '练功新人'
        elif dazuo < 500:
            honor = '练功油条'
        elif dazuo < 1000:
            honor = '练功入神'
        elif dazuo < 1500:
            honor = '练功狂魔'
        else:
            honor = '练功肝帝'
        return honor

    def killhonor(self) -> str:
        kill = self.killnum
        if kill < 100:
            honor = '小杀一下'
        elif kill < 500:
            honor = '百人刀魂'
        elif kill < 1000:
            honor = '刀不过千'
        elif kill < 2000:
            honor = '千军亦死'
        elif kill < 3000:
            honor = '杀人狂魔'
        elif kill < 5000:
            honor = '令人发指'
        elif kill < 10000:
            honor = '亡魂魔神'
        else:
            honor = '一将功成万骨枯'
        return honor

    def getInfo(self):
        self.upSql()
        if self.isBiguan():
            bg = '闭关中'
        else:
            bg = '出战中'
        return f'姓名:{self.name}\n境界:{self.xianlevel()}\n称号:{self.honor()}\n性别:{self.sex}\n血量:{self.HP}\n蓝量:{self.MP}\n攻击:{self.attack}\n防御:{self.defense}\n速度:{self.speed}\n灵气:{self.experience}/{self.level ** 2 * 100}\n灵石:{self.gold}\n闭关:{bg}\n修仙年份:{int((time.time() - self.stime) / 86400)}天'

    def dazuo(self) -> (int, int):
        exp = random.randint(-3, 50)
        status = 0
        if exp < 0:
            exp *= random.randint(2, 5) * self.level
            status = -1
        elif exp == 0:
            if 0 == random.randint(0, 100):
                self.level -= 1
                status = -3
            else:
                exp = -20
                exp *= self.level * random.randint(2, 5)
                status = -2
        elif exp in (40, 41):
            exp = exp * random.randint(5, 8) * self.level // 8
            status = 1
        elif exp in (49, 50):
            exp = self.level * exp * random.randint(3, 5)
            status = 2
        else:
            exp = exp * self.level // 8
            status = 0
        self.dazuonum += 1
        self.experience += exp
        return exp, status

    def incSign(self) -> bool:
        if self.signStatus == 0:
            self.gold += 50
            self.experience += self.level * 5
            self.signStatus = 1
            self.upLevel()
            return True
        return False

    def work(self) -> int:
        g = random.randint(10, 50)
        self.worknum += 1
        self.gold += g
        return g

    def fishing(self) -> (int, int, bool):
        if self.gold < 50:
            return (0, 0, False)
        self.gold -= 50
        self.fishnum += 1
        g = random.randint(1, 30)
        e = random.randint(1, 50)
        if g + e < 40:
            return (g, e, False)
        elif g + e <= 60:
            g = g // 3
            e = e // 3
        elif g + e > 78:
            g *= self.level * 50
            e *= 50 * self.level
        else:
            g *= 20
            e *= 20
        self.gold += g
        self.experience += e
        self.upLevel()
        return (g, e, True)

    def upLevel(self):
        if self.experience > self.level ** 2 * 100:
            self.experience -= self.level ** 2 * 100
            self.level += 1
            self.attack += 10 * self.level
            self.defense += 5 * self.level
            self.speed += 3 * self.level
            self.MP += 10 * self.level
            self.HP += 30 * self.level

    def supergoldToField(self) -> bool:
        if self.gold >= 2000:
            self.gold -= random.randint(1500, 2000)
            self.attack += random.randint(100, 300)
            self.defense += random.randint(100, 300)
            self.speed += random.randint(100, 300)
            self.upSql()
            return True
        return False

    def goldToField(self) -> bool:
        if self.gold >= 20:
            self.gold -= random.randint(15, 20)
            self.attack += random.randint(0, 3)
            self.defense += random.randint(0, 3)
            self.speed += random.randint(0, 3)
            self.upSql()
            return True
        return False

    def kaigua(self):
        self.HP += 50
        self.MP += 50
        self.attack += 1000
        self.defense += 1000
        self.speed += 1000
        self.experience += 100000
        self.gold += 1000

    def isLive(self) -> bool:
        return True if self.HP > 0 else False

    def upSql(self):
        con = sqlite3.connect('data/xiuxian.data')
        cur = con.cursor()
        cur.execute(
            'update Role set name=?,gold=?,attack=?,defense=?,speed=?,HP=?,MP=?,level=?,experience=?,sex=?,sign=? where uid=?',
            (self.name, self.gold, self.attack, self.defense, self.speed, self.HP, self.MP, self.level, self.experience,
             self.sex, self.signStatus, self.uid))
        cur.execute('update chenghao set kill=?,fish=?,dazuo=?,work=? where uid=?',
                    (self.killnum, self.fishnum, self.dazuonum, self.worknum, self.uid))
        con.commit()
        cur.close()
        con.close()

    def getSql(self):
        con = sqlite3.connect('data/xiuxian.data')
        cur = con.cursor()
        cur.execute('select * from Role where uid =?', (self.uid,))
        con.commit()
        value = cur.fetchall()
        if len(value) != 0:
            value = value[0]
            _, self.name, self.gold, self.attack, self.defense, self.speed, self.HP, self.MP, self.level, self.experience, self.stime, self.sex, self.signStatus = value
            if self.HP < 0:
                self.HP = 0
            if self.MP < 0:
                self.MP = 0
            if self.gold < 0:
                self.gold = 0
        else:
            cur.execute(
                'insert into Role(uid,name,gold,attack,defense,speed,HP,MP,level,experience,stime,sex,sign) values(?,?,?,?,?,?,?,?,?,?,?,?,?)',
                (self.uid, self.name, self.gold, self.attack, self.defense, self.speed, self.HP, self.MP, self.level,
                 self.experience, self.stime, self.sex, self.signStatus))
            con.commit()
        cur.execute('select * from chenghao where uid =?', (self.uid,))
        con.commit()
        value = cur.fetchall()
        if len(value) != 0:
            value = value[0]
            _, self.killnum, self.fishnum, self.dazuonum, self.worknum = value
        else:
            cur.execute('insert into chenghao(uid,kill,fish,dazuo,work) values(?,?,?,?,?)',
                        (self.uid, self.killnum, self.fishnum, self.dazuonum, self.worknum))
            con.commit()
        cur.close()
        con.close()

    def __del__(self):
        self.upLevel()
        # 更新数据
        self.upSql()


def num_to_char(num: int):
    num_dict = {"0": u"零", "1": u"一", "2": u"二", "3": u"三", "4": u"四", "5": u"五", "6": u"六", "7": u"七", "8": u"八",
                "9": u"九"}
    return num_dict[str(num)]

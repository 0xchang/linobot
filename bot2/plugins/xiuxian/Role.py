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

class XianRole:
    def __init__(self,uid:int,name:str='无名氏',sex:str='男'):
        self.uid=uid
        self.name=name
        self.gold=0
        self.attack=20
        self.defense=10
        self.speed=6
        self.HP=100
        self.MP=50
        self.level=1
        self.experience=0
        self.stime=int(time.time())
        self.sex=sex
        self.signStatus=0
        self.getSql()

    def setSex(self,sex:str):
        self.sex=sex

    def getGold(self):
        return self.gold

    def setGold(self,gold:int):
        self.gold=gold

    def setName(self,name:str):
        self.name=name

    def getName(self):
        return self.name

    def upHPMP(self)->bool:
        if self.gold<20:
            return False
        else:
            self.gold-=20
            self.MP+=30
            self.HP+=50
            return True

    def kill(self,u1)->str:
        if self.MP<=0:
            return '你的蓝量不足，不能攻击'
        if self.HP<=0:
            self.gold-=15
            return f'你的血量为0,你掉了一些15金子'
        if u1.HP<=0:
            u1.gold-=25
            self.gold+=25
            return '你要攻击的人的血量为0,你捡起来了他的25金子'
        if self.speed>=u1.speed:
            #先攻击
            at1=self.attack-u1.defense
            at2=u1.attack-self.defense
            at1 = 0 if at1 <= 0 else at1
            at2 = 0 if at2 <= 0 else at2
            u1.HP-=at1
            if u1.HP>0:
                self.HP-=at2
                if self.HP>0:
                    return f'回合结束！你掉了{at2}血，他掉了{at1}血'
                self.gold-=25
                u1.gold+=25
                return '你死了，他捡起了你的25金'
            u1.gold-=25
            self.gold+=25
            return '他死了，你捡起了他的25金'
        else:
            #后攻击
            at1=u1.attack-self.defense
            at1=0 if at1<=0 else at1
            at2=self.attack-u1.defense
            at2 = 0 if at2 <= 0 else at2
            self.HP-=at1
            if self.HP>0:
                u1.HP-=at2
                if u1.HP>0:
                    return f'回合结束！你掉了{at1}血，他掉了{at2}血'
                self.gold+=25
                u1.gold-=25
                return '他死了，你捡起了他的25金'
            u1.gold+=25
            self.gold-=25
            return '你死了，他捡起了你的25金'


    def getInfo(self):
        self.upSql()
        return f'姓名:{self.name}\n性别:{self.sex}\n血量:{self.HP}\n蓝量:{self.MP}\n攻击:{self.attack}\n防御:{self.defense}\n速度:{self.speed}\n等级:{self.level}\n经验:{self.experience}\n金币:{self.gold}\n修仙年份:{int((time.time()-self.stime)/86400)}天'

    def incSign(self)->bool:
        if self.signStatus==0:
            self.gold+=50
            self.experience+=self.level*5
            self.signStatus = 1
            self.upLevel()
            return True
        return False

    def work(self)->int:
        g=random.randint(10,50)
        self.gold+=g
        return g

    def fishing(self)->(int,int):
        g=random.randint(5,20)
        e=random.randint(5,10)
        self.gold+=g
        self.experience+=e
        self.upLevel()
        return (g,e)

    def upLevel(self):
        if self.experience>self.level*100:
            self.experience-=self.level*100
            self.level+=1
            self.attack+=10
            self.defense+=5
            self.speed+=3
            self.MP+=30
            self.HP+=50

    def goldToField(self)->bool:
        if self.gold>=15:
            self.gold-=random.randint(12,15)
            self.attack+=random.randint(0,3)
            self.defense+=random.randint(0,3)
            self.speed+=random.randint(0,3)
            self.HP+=random.randint(0,3)
            self.MP+=random.randint(0,3)
            self.upSql()
            return True
        return False

    def isLive(self)->bool:
        return True if self.HP>0 else False

    def upSql(self):
        con=sqlite3.connect('data/xiuxian.data')
        cur=con.cursor()
        cur.execute('update Role set name=?,gold=?,attack=?,defense=?,speed=?,HP=?,MP=?,level=?,experience=?,sex=?,sign=? where uid=?',
                    (self.name,self.gold,self.attack,self.defense,self.speed,self.HP,self.MP,self.level,self.experience,self.sex,self.signStatus,self.uid))
        con.commit()
        cur.close()
        con.close()

    def getSql(self):
        con = sqlite3.connect('data/xiuxian.data')
        cur = con.cursor()
        cur.execute('select * from Role where uid =?', (self.uid,))
        con.commit()
        value = cur.fetchall()
        if len(value)!=0:
            value=value[0]
            _,self.name,self.gold,self.attack,self.defense,self.speed,self.HP,self.MP,self.level,self.experience,self.stime,self.sex,self.signStatus=value
        else:
            cur.execute('insert into Role(uid,name,gold,attack,defense,speed,HP,MP,level,experience,stime,sex,sign) values(?,?,?,?,?,?,?,?,?,?,?,?,?)',
                        (self.uid,self.name,self.gold,self.attack,self.defense,self.speed,self.HP,self.MP,self.level,self.experience,self.stime,self.sex,self.signStatus))
            con.commit()
        cur.close()
        con.close()

    def __del__(self):
        self.upLevel()
        #更新数据
        self.upSql()
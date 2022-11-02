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

    def clear(self):
        self.gold=0
        self.attack=20
        self.defense=10
        self.speed=6
        self.HP=100
        self.MP=50
        self.level=1
        self.experience=0
        self.stime=int(time.time())
        self.signStatus=0
        self.upSql()

    def biguan(self):
        con=sqlite3.connect('data/xiuxian.data')
        cur=con.cursor()
        cur.execute('select * from biguan where uid=?',(self.uid,))
        con.commit()
        va=cur.fetchall()
        if len(va)==0:
            cur.execute('insert into biguan(uid,xtime) values(?,?)',(self.uid,int(time.time())))
            con.commit()
            self.experience+=500
            now=int(time.time())
        else:
            va=va[0][1]
            if int(time.time())-va>30*60:
                cur.execute('update biguan set xtime=? where uid=?',(int(time.time()),self.uid))
                con.commit()
                self.experience+=500
                now=int(time.time())
            else:
                now=int(time.time())-va
        cur.close()
        con.close()
        return now

    def isBiguan(self):
        con=sqlite3.connect('data/xiuxian.data')
        cur=con.cursor()
        cur.execute('select * from biguan where uid=?',(self.uid,))
        con.commit()
        va = cur.fetchall()
        cur.close()
        con.close()
        if len(va)==0:
            return False
        else:
            va=va[0][1]
            if int(time.time())-va>30*60:
                return False
            else:
                return True

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
            return f'你的血量为0,你掉了一些15灵石'
        self.MP-=2
        u1.MP-=2
        if u1.HP<=0:
            u1.gold-=25
            self.gold+=25
            return '你要攻击的人的血量为0,你捡起来了他的25灵石'
        if self.speed>=u1.speed:
            #先攻击
            at1=self.attack-u1.defense
            at2=u1.attack-self.defense
            at1 = 0 if at1 <= 0 else at1*5
            at2 = 0 if at2 <= 0 else at2*5
            u1.HP-=at1
            if u1.HP>0:
                self.HP-=at2
                if self.HP>0:
                    return f'回合结束！你掉了{at2}血，他掉了{at1}血'
                self.gold-=25
                u1.gold+=25
                return '你死了，他捡起了你的25灵石'
            u1.gold-=25
            self.gold+=25
            return '他死了，你捡起了他的25灵石'
        else:
            #后攻击
            at1=u1.attack-self.defense
            at1=0 if at1<=0 else at1*5
            at2=self.attack-u1.defense
            at2 = 0 if at2 <= 0 else at2*5
            self.HP-=at1
            if self.HP>0:
                u1.HP-=at2
                if u1.HP>0:
                    return f'回合结束！你掉了{at1}血，他掉了{at2}血'
                self.gold+=25
                u1.gold-=25
                return '他死了，你捡起了他的25灵石'
            u1.gold+=25
            self.gold-=25
            return '你死了，他捡起了你的25灵石'



    def xianlevel(self)->str:
        level=self.level
        n0=level//10
        n1=level%10
        honor=''
        if n0<1:
            honor+='练气期'
        elif n0<2:
            honor+='筑基期'
        elif n0<3:
            honor+='结丹期'
        elif n0<4:
            honor+='金丹期'
        elif n0<5:
            honor+='元婴期'
        elif n0<6:
            honor += '出窍期'
        elif n0<7:
            honor+='化神期'
        elif n0<8:
            honor+='渡劫期'
        elif n0<9:
            honor+='真仙'
        honor+=f'{num_to_char(n1)}阶'
        return honor

    def honor(self):
        level=self.level
        honor=''
        if level<20:
            honor='无名小卒'
        elif level<40:
            honor='有所小成'
        elif level<60:
            honor='有所大成'
        elif level<80:
            honor='扬名立万'
        elif level<100:
            honor='名动天下'
        return honor

    def getInfo(self):
        self.upSql()
        if self.isBiguan():
            bg='闭关中'
        else:
            bg='出战中'
        return f'姓名:{self.name}\n境界:{self.xianlevel()}\n称号:{self.honor()}\n性别:{self.sex}\n血量:{self.HP}\n蓝量:{self.MP}\n攻击:{self.attack}\n防御:{self.defense}\n速度:{self.speed}\n灵气:{self.experience}/{self.level*100}\n灵石:{self.gold}\n闭关:{bg}\n修仙年份:{int((time.time()-self.stime)/86400)}天'

    def dazuo(self)->int:
        exp=random.randint(-20,40)
        self.experience+=exp
        return exp

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

    def fishing(self)->(int,int,bool):
        if self.gold<5:
            return (0,0,False)
        self.gold-=5
        g=random.randint(1,20)
        e=random.randint(1,10)
        if g+e<15:
            return (g,e,False)
        elif g+e<=20:
            g=g//3
            e=e//3
        elif g+e>28:
            g*=3
            e*=3
        self.gold+=g
        self.experience+=e
        self.upLevel()
        return (g,e,True)

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

def num_to_char(num:int):
    num_dict = {"0": u"零", "1": u"一", "2": u"二", "3": u"三", "4": u"四", "5": u"五", "6": u"六", "7": u"七", "8": u"八",
                "9": u"九"}
    return num_dict[str(num)]

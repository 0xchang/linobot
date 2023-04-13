#!/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2023/2/16 14:44
@author: 0xchang
@E-mail: oxchang@163.com
@file: __init__.py
@Github: https://github.com/0xchang
"""
from nonebot import on_notice
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
import asyncio
from nonebot.adapters.onebot.v11 import GroupIncreaseNoticeEvent
from nonebot import on_command, on_keyword, on_fullmatch, on_startswith
from nonebot.params import CommandArg
from urllib.parse import quote
from nonebot import get_bot
import time
import urllib.parse
import requests
from .aior18 import getdata

welcom = on_notice()
speak_cmd = on_command('发话', priority=100)
fancmd = on_command('看番', priority=100)
remind1 = on_keyword({'提醒'}, priority=100, block=False)
col_n = on_command('黑色', aliases={'红色', '粉色', '紫色', '黄色', '初春', '冬梅', '高级灰', '黄昏', '科技感',
                                  '马卡龙', '霓虹闪烁', '日出', '盛夏', '糖果缤纷', '晚秋', '夜空', '粉黛', '朝夕', '潮流'}, priority=282)
color_name = on_fullmatch('昵称颜色', priority=100)
group_name = on_command('群昵称', priority=100)
r18 = on_fullmatch(('r18', 'R18'), priority=100, block=False)
pr18 = on_fullmatch(('pr18', 'PR18', 'Pr18'), priority=100, block=False)
seci = on_startswith(('涩词', 'seci', '塞词'), priority=100, block=False)
grouphelp = on_fullmatch('群帮助', priority=100)


@grouphelp.handle()
async def _():
    helpmenu = '''
    ***群帮助***
发话--让假人说话
看番--看动漫
提醒--告诉你准备做啥
(黑色/粉色...名字)--自助合成昵称
昵称颜色--显示各种群昵称颜色
群昵称--改掉自己的群昵称
r18--xx
pr18-xx
seci-xx'''
    await grouphelp.finish(helpmenu)


@welcom.handle()
async def _(event: GroupIncreaseNoticeEvent):
    user = event.get_user_id()
    at_ = f"欢迎[CQ:at,qq={user}]"
    msg = at_ + '加入大家庭,你可以使用/帮助来获取帮助信息'
    msg = Message(msg)
    await welcom.finish(msg)


@speak_cmd.handle()
async def _(argcom: Message = CommandArg()):
    txt = argcom.extract_plain_text().strip().replace(' ', '')
    mess = f'[CQ:tts,text={txt}]'
    print(mess)
    await speak_cmd.finish(Message(mess))


@remind1.handle()
async def _(event: GroupMessageEvent):
    mess = event.get_plaintext()
    mess = mess.split('提醒')
    if (not mess[0].strip().isdigit()) or mess[1].strip() == '':
        await remind1.finish(Message('格式不对，请输入时间 提醒 事件,例如30 提醒 记得吃饭(30分钟后提醒吃饭)'))
    t = int(mess[0])
    await remind1.send(Message('已添加到提醒事项中!'))
    await asyncio.sleep(t * 60)
    await remind1.finish(Message(f'\n提醒通知:\n记得{mess[1]}哦!'), at_sender=True)


@fancmd.handle()
async def _(argcom: Message = CommandArg()):
    word = argcom.extract_plain_text()
    wordurl = 'https://www.agemys.net/search?query=' + quote(word) + '&page=1'
    mess = wordurl
    await fancmd.finish(Message(mess))


@group_name.handle()
async def _(event: GroupMessageEvent, argcom: Message = CommandArg()):
    bot = get_bot()
    # 保留颜色符号，没有改成彩色名字
    color = ''
    print(event.get_plaintext())
    uid = event.get_user_id()
    gid = event.group_id
    argcom = argcom.extract_plain_text()
    argcom = argcom.strip()
    newname = color + argcom
    if len(newname.encode()) >= 60:
        await group_name.finish(Message('名字有点长了哦，短一点试试吧'))
    await bot.call_api('set_group_card',
                       group_id=gid,
                       user_id=uid,
                       card=newname)
    await group_name.finish(Message(f'成功改群名为{argcom}'))


@color_name.handle()
async def _():
    color0 = '<&ÿĀĀĀ>黑色 \n<&ÿÿ5@>红色 \n<&ÿÿ]>粉色 \n<&ÿÒUÐ>紫色 \n<&ÿÿÏP>黄色 \n<%ĀĀÐ>初春 \n'
    color1 = '<%ĀĀÑ>冬梅 \n<%ĀĀÒ>高级灰 \n<%ĀĀÓ>黄昏 \n<%ĀĀÔ>科技感 \n<%ĀĀÕ>马卡龙 \n<%ĀĀÖ>霓虹闪烁 \n'
    color2 = '<%ĀĀ×>日出 \n<%ĀĀØ>盛夏 \n<%ĀĀÙ>糖果缤纷 \n<%ĀĀÚ>​晚​秋 \n<%ĀĀÛ>夜空 \n<%ĀĀÜ>粉黛 \n'
    color3 = '<%ĀĀÝ>朝夕 \n<%ĀĀÞ>潮流 ​ \n'
    mess = color0 + color1 + color2 + color3 + '\n以上特殊代码+名字即可，仅适用于群昵称'
    await color_name.finish(Message(mess))


@col_n.handle()
async def _(event: GroupMessageEvent, argcom: Message = CommandArg()):
    name = argcom.extract_plain_text().strip()
    gmess = event.get_plaintext()
    col_dict = {'红色': '<&ÿÿ5@>', '黑色': '<&ÿĀĀĀ>', '粉色': '<&ÿÿ]>',
                '紫色': '<&ÿÒUÐ>', '黄色': '<&ÿÿÏP>', '初春': '<%ĀĀÐ>',
                '冬梅': '<%ĀĀÑ>', '高级灰': '<%ĀĀÒ>', '黄昏': '<%ĀĀÓ>',
                '科技感': '<%ĀĀÔ>', '马卡龙': '<%ĀĀÕ>', '霓虹闪烁': '<%ĀĀÖ>',
                '日出': '<%ĀĀ×>', '盛夏': '<%ĀĀØ>', '糖果缤纷': '<%ĀĀÙ>',
                '晚秋': '<%ĀĀÚ>​', '夜空': '<%ĀĀÛ>', '粉黛': '<%ĀĀÜ>',
                '朝夕': '<%ĀĀÝ>', '潮流': '<%ĀĀÞ>'}
    for key in col_dict.keys():
        if gmess.startswith(key):
            await col_n.send(Message(f'{col_dict[key]}{name}'))


@r18.handle()
async def _(bot: Bot):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    imgurl = requests.get(url='https://moe.anosu.top/r18/', headers=headers, allow_redirects=False).headers[
        'Location']
    time.sleep(0.5)
    mid = (await pr18.send(Message(f'图片太se发不出来，给你网址自己看吧\n{imgurl}')))['message_id']
    await asyncio.sleep(30)
    await bot.delete_msg(message_id=mid)


@pr18.handle()
async def _(bot: Bot):
    flag = False
    data = await getdata('https://moe.anosu.top/img/?sort=r18&type=json')
    imgurl = data['pics'][0]
    time.sleep(0.5)
    try:
        mid = (await pr18.send(Message(f'[CQ:image,file={imgurl}]')))['message_id']
        nmid = (await pr18.send(Message(f'图片原网址,不清晰可转移\n{imgurl}')))['message_id']
        flag = True
    except:
        mid = (await pr18.send(Message(f'图片太se发不出来，给你网址自己看吧\n{imgurl}')))['message_id']
    await asyncio.sleep(30)
    if flag:
        await bot.delete_msg(message_id=nmid)
    await bot.delete_msg(message_id=mid)


@seci.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    flag = False
    arg = event.get_plaintext().split()[1]
    arg = urllib.parse.urlencode({'keyword': arg})
    resp = await getdata(f'https://image.anosu.top/pixiv/json?{arg}')
    imgurl = resp[0]['url']
    try:
        mid = (await pr18.send(Message(f'[CQ:image,file={imgurl}]')))['message_id']
        nmid = (await pr18.send(Message(f'图片原网址,不清晰可转移\n{imgurl}')))['message_id']
        flag = True
    except:
        mid = (await pr18.send(Message(f'图片太se发不出来，给你网址自己看吧\n{imgurl}')))['message_id']
    await asyncio.sleep(30)
    if flag:
        await bot.delete_msg(message_id=nmid)
    await bot.delete_msg(message_id=mid)

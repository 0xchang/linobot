import time

from nonebot.permission import SUPERUSER
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from nonebot.adapters.onebot.v11 import GROUP_ADMIN, GROUP_OWNER
from nonebot.adapters.onebot.v11 import Event
from nonebot.adapters.onebot.v11.message import Message
import random


superuser = on_command("测试超管", permission=SUPERUSER,priority=3)
@superuser.handle()
async def _():
    await superuser.send("超管命令测试成功")

power = on_command("测试权限")
@power.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    if await GROUP_ADMIN(bot, event):
        await power.send("管理员测试成功")
    elif await GROUP_OWNER(bot, event):
        await power.send("群主测试成功")
    else:
        await power.send("群员测试成功")

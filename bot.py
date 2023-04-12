#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter
from nonebot.log import logger, default_format
from pathlib import Path

# Custom your logger
# 
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

if not os.path.exists('log'):
    os.mkdir('log')

logger.add("log/error.log",
           rotation="00:00",
           diagnose=False,
           level="ERROR",
           format=default_format)

# You can pass some keyword args config to init function
nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

nonebot.load_builtin_plugins("echo")
nonebot.load_plugin(Path("bot2/plugins/eat/"))
nonebot.load_plugin(Path('bot2/plugins/bili/'))
nonebot.load_plugin(Path("bot2/plugins/mgroup/"))
nonebot.load_plugin(Path("bot2/plugins/help/"))
nonebot.load_plugin(Path("bot2/plugins/wife/"))
nonebot.load_plugin(Path("bot2/plugins/yanxi/"))
# 修仙插件,后面补上
# nonebot.load_plugin(Path("bot2/plugins/xiuxian/"))

nonebot.load_plugin('nonebot_plugin_remake')
nonebot.load_plugin('nonebot_plugin_simplemusic')
nonebot.load_plugin('nonebot_plugin_petpet')
nonebot.load_plugin('nonebot_plugin_smart_reply')
nonebot.load_plugin('nonebot_plugin_setu4')
nonebot.load_plugin('nonebot_plugin_tarot')
nonebot.load_plugin('nonebot_plugin_crazy_thursday')
nonebot.load_plugin('nonebot_plugin_caiyunai')
# Please DO NOT modify this file unless you know what you are doing!
# As an alternative, you should use command `nb` or modify `pyproject.toml` to load plugins


# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...


if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")

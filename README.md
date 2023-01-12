# linobot
一个bilibili和qq机器人，主要借助nonebot2、bilibili-api、go-cqhttp来实现的。

## 安装
go-cqhttp默认安装即可

### 本项目
**推荐使用conda安装python环境方便多版本管理,python>3.8**

* ubuntu系统先看https://github.com/noneplugin/nonebot-plugin-imageutils

```
git clone
cd linobot
pip install -r requirements.txt
nb plugin install nonebot_plugin_apscheduler
nb plugin install nonebot_plugin_simplemusic
nb plugin install nonebot_plugin_remake
nb plugin install nonebot_plugin_imageutils
nb plugin install nonebot_plugin_petpet
nb plugin install nonebot-plugin-smart-reply
nb plugin install nonebot-plugin-setu4
nb plugin install nonebot-plugin-tarot
nb plugin install nonebot-plugin-crazy-thursday
nb plugin install nonebot_plugin_caiyunai
```
### 修改.env文件内容
```shell
ENVIRONMENT=dev
APSCHEDULER_CONFIG={"apscheduler.timezone": "Asia/Shanghai"}
TAROT_PATH="./data/tarot"
CHAIN_REPLY=false
caiyunai_apikey=xxxxxxxxxxxxxxx(参照https://github.com/noneplugin/nonebot-plugin-caiyunai)
```

```shell
nb run
#注意.env.dev中的端口需和go-cqhttp当中的端口一致
```

### 更新2023-1-8
* 增加提醒功能
* 由于插件问题,移除nonebot-plugin-aidraw插件

### 更新2022-11-9
* 使用`nonebot_plugin_simplemusic`插件，地址https://github.com/noneplugin/nonebot-plugin-simplemusic

* 使用`nonebot_plugin_remake`插件，地址https://github.com/noneplugin/nonebot-plugin-remake

* 使用`nonebot_plugin_petpet`插件，地址https://github.com/noneplugin/nonebot-plugin-petpet

* 使用`nonebot_plugin_imageutils`，地址https://github.com/noneplugin/nonebot-plugin-imageutils

* 使用`nonebot-plugin-smart-reply`，地址https://github.com/Special-Week/nonebot_plugin_smart_reply

* 使用`nonebot-plugin-setu4`，地址https://github.com/Special-Week/nonebot_plugin_setu4

* 使用`nonebot-plugin-tarot`，地址https://github.com/MinatoAquaCrews/nonebot_plugin_tarot

* 使用`nonebot-plugin-aidraw`，地址https://github.com/A-kirami/nonebot-plugin-aidraw

* 使用`nonebot_plugin_crazy_thursday`，地址https://github.com/MinatoAquaCrews/nonebot_plugin_crazy_thursday

* 使用`nonebot_plugin_caiyunai`，地址https://github.com/noneplugin/nonebot-plugin-caiyunai

### 更新2022-11-8
* 增加银行系统

### 更新2022-11-5
* 优化代码，添加投稿，置顶功能。
* 优化修仙功能。

## 请大家关注b站狸诺酱lino
* https://space.bilibili.com/3461578707962799?spm_id_from=333.337.0.0


# linobot
一个bilibili和qq机器人，主要借助nonebot2、bilibili-api、go-cqhttp来实现的。

## 安装
go-cqhttp默认安装即可

### 本项目
**推荐使用conda安装python环境方便多版本管理,python>3.8**
```
git clone
cd linobot
pip install -r requirements.txt
nb plugin install nonebot_plugin_apscheduler
#修改.env.dev文件内容
nb run
#注意.env.dev中的端口需和go-cqhttp当中的端口一致
```

### 更新2022-11-5
优化代码，添加投稿，置顶功能。
优化修仙功能。

## 请大家关注b站狸诺酱lino，https://space.bilibili.com/3461578707962799?spm_id_from=333.337.0.0


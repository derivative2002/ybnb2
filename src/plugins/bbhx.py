from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11.message import Message, MessageSegment

import random
__plugin_name__ = 'bbhx'
__plugin_usage__ = '用法： 带节奏'

printer0 = on_command("骄阳", priority=1, aliases={"阳宝", "阳宝宝", "骄阳想要求导导", "陽寶", "驕陽想要求導導"})
printer1 = on_command("土豆", priority=1, aliases={"土子哥", "无拘狂热者"})
printer2 = on_command("bbhx", priority=1, aliases={"笨笨", "bbhx", "节奏帝", "带节奏", "来点节奏", "潘天瑞"})
printer3 = on_command("ba", priority=1, aliases={"bahfahh", "博文哥", "博文", "巴赫发呵呵", "台服塔达林老前辈"})
printer4 = on_command("qqoo", priority=1, aliases={"qqoo2452", "q宝", "q寶", "小島隱士", "臭臭哦哦"})
printer5 = on_command("果果", priority=1, aliases={"果", "憨批果", "塔达林的红果果", "塔达林的红呆呆", "好聪明的红果果", "果呆呆"})
printer6 = on_command("prismcharge", priority=1, aliases={"p姓主播", "和牛", "能量和弦很牛", "牛牛", "牛子哥", "牛哥", "普瑞兹米恰鸡", "卡比", "卡b"})
printer7 = on_command("半辈辛酸", priority=1, aliases={"半圣", "bbxs", "半辈", "虎牙一哥", "虎牙半辈"})

@printer0.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    rand_num = random.randint(0, 1)
    if rand_num == 0:
        await printer0.finish("可恶!被你发现了！")
    if rand_num == 1:
        await printer0.finish("可恶!被你发现了！")

@printer1.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    rand_num = random.randint(0, 6)
    if rand_num == 0:
        await printer1.send("你觉得你很有理？")
    if rand_num == 1:
        await printer1.send("啊对对对")
    if rand_num == 2:
        await printer1.send("我知道他是舰长我还是要踢了他")
    if rand_num == 3:
        await printer1.send("滚吧")
    if rand_num == 4:
        await printer1.send("我办的比赛我说了算")
    if rand_num == 5:
        await printer1.send("你觉得你很有理？")
    if rand_num == 6:
        await printer1.send("你觉得你很有理？")

@printer2.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    rand_num = random.randint(0, 8)
    if rand_num == 0:
        msg = MessageSegment.image("file:///E:/program/qqbot_yb/ybnb2/image/bbhx/bbhx0.jpg")
        await printer2.send(msg)
    if rand_num == 1:
        msg = MessageSegment.image("file:///E:/program/qqbot_yb/ybnb2/image/bbhx/bbhx1.jpg")
        await printer2.send(msg)
    if rand_num == 2:
        msg = MessageSegment.image("file:///E:/program/qqbot_yb/ybnb2/image/bbhx/bbhx2.jpg")
        await printer2.send(msg)
    if rand_num == 3:
        msg = MessageSegment.image("file:///E:/program/qqbot_yb/ybnb2/image/bbhx/bbhx3.jpg")
        await printer2.send(msg)
    if rand_num == 4:
        msg = MessageSegment.image("file:///E:/program/qqbot_yb/ybnb2/image/bbhx/bbhx4.jpg")
        await printer2.send(msg)
    if rand_num == 5:
        msg = MessageSegment.image("file:///E:/program/qqbot_yb/ybnb2/image/bbhx/bbhx5.jpg")
        await printer2.send(msg)
    if rand_num == 6:
        msg = MessageSegment.image("file:///E:/program/qqbot_yb/ybnb2/image/bbhx/bbhx6.jpg")
        await printer2.send(msg)
    if rand_num == 7:
        msg = MessageSegment.image("file:///E:/program/qqbot_yb/ybnb2/image/bbhx/bbhx7.jpg")
        await printer2.send(msg)
    if rand_num == 8:
        msg = MessageSegment.image("file:///E:/program/qqbot_yb/ybnb2/image/bbhx/bbhx8.jpg")
        await printer2.send(msg)

@printer3.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    rand_num = random.randint(0, 6)
    if rand_num == 0:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\bahfahh\\ba0.jpg")
        await printer3.send(msg)
    if rand_num == 1:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\bahfahh\\ba1.jpg")
        await printer3.send(msg)
    if rand_num == 2:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\bahfahh\\ba2.jpg")
        await printer3.send(msg)
    if rand_num == 3:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\bahfahh\\ba3.jpg")
        await printer3.send(msg)
    if rand_num == 4:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\bahfahh\\ba4.jpg")
        await printer3.send(msg)
    if rand_num == 5:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\bahfahh\\ba5.jpg")
        await printer3.send(msg)
    if rand_num == 6:
        await printer3.send("星際合作 apm 300")

@printer4.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    rand_num = random.randint(0, 9)
    if rand_num == 0:
        await printer4.send("給予世界痛楚")
    if rand_num == 1:
        await printer4.send("神羅天征")
    if rand_num == 2:
        await printer4.send("沒關係陽寶")
        await printer4.finish("總會有辦法的")
    if rand_num == 3:
        await printer4.send("滚吧")
    if rand_num == 4:
        await printer4.send("挺好的")
    if rand_num == 5:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\qqoo\\qqoo0.jpg")
        await printer4.finish(msg)
    if rand_num == 6:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\qqoo\\qqoo1.jpg")
        await printer4.finish(msg)
    if rand_num == 7:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\qqoo\\qqoo2.jpg")
        await printer4.finish(msg)
    if rand_num == 8:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\qqoo\\qqoo3.jpg")
        await printer4.finish(msg)
    if rand_num == 9:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\qqoo\\qqoo4.png")
        await printer4.finish(msg)

@printer6.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    rand_num = random.randint(0, 24)
    if rand_num == 0:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\prismcharge\\p0.jpg")
        await printer6.send(msg)
    if rand_num == 1:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\prismcharge\\p1.jpg")
        await printer6.send(msg)
    if rand_num == 2:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\prismcharge\\p2.jpg")
        await printer6.send(msg)
    if rand_num == 3:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\prismcharge\\p3.jpg")
        await printer6.send(msg)
    if rand_num == 4:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\prismcharge\\p4.jpg")
        await printer6.send(msg)
    if rand_num == 5:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\prismcharge\\p5.jpg")
        await printer6.send(msg)
    if rand_num == 6:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\prismcharge\\p6.jpg")
        await printer6.send(msg)
    if rand_num == 7:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\prismcharge\\p7.jpg")
        await printer6.send(msg)
    if rand_num == 8:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\prismcharge\\p8.jpg")
        await printer6.send(msg)
    if rand_num == 9:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\prismcharge\\p9.jpg")
        await printer6.send(msg)
    if rand_num == 10:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\prismcharge\\p10.jpg")
        await printer6.send(msg)
    if rand_num == 11:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\prismcharge\\p11.jpg")
        await printer6.send(msg)
    if rand_num == 12:
        msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\\prismcharge\\p12.jpg")
        await printer6.send(msg)

@printer7.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    msg = MessageSegment.image("file:///E:\\program\\qqbot_yb\\ybnb2\\image\bbxs\\bbxs0.jpg")
    await printer7.send(msg)
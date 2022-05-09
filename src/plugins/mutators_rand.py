import random

from nonebot import on_regex
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11.message import MessageSegment, Message
from nonebot.params import RegexGroup

__plugin_name__ = 'mutators_rand'
__plugin_usage__ = '用法：随机因子'

reg0 = on_regex(pattern="(随机因子)(\d+)", priority=1)
reg1 = on_regex(pattern="(裂隙随)(\d+)", priority=1)
reg2 = on_regex(pattern="(风暴随)(\d+)", priority=1)
reg3 = on_regex(pattern="(\d+)(件套)", priority=1)
reg4 = on_regex(pattern="(风暴裂隙随)(\d+)", priority=1)

Mutators = ["行尸走肉", "丧尸大战", "暗无天日", "时间扭曲", "速度狂魔", "强磁雷场", "晶矿护盾", "减伤屏障", "复仇战士", "闪避机动", "焦土政策", "岩浆爆发", "自毁程序", "进攻部署", "异形寄生", "激光钻机", "超远视距", "相互摧毁", "来去无踪", "震荡攻击", "给我死吧", "时空立场", "虚空裂隙", "龙卷风暴", "轨道轰炸", "净化光束", "暴风雪", "无边恐惧", "光子过载", "扫雷专家", "虚空重生者", "核弹打击", "生命汲取", "灵能报表", "飞弹大战", "力量蜕变", "伤害散射", "黑死病", "强行征用", "风暴英雄", "鼓舞人心", "坚强意志", "双重压力", "同化体", "默哀"]

@reg0.handle()
async def handle_first_receive(bot: Bot, event: Event, msg: tuple = RegexGroup()):
    send_msg = Message(MessageSegment.text("来点因子：\n"))
    rand_times = int(msg[1])
    l1 = random.sample(range(0, 43), rand_times)
    for i in range(0, rand_times):
        send_msg = send_msg + "    " + MessageSegment.text(Mutators[l1[i]]) + "\n"
    send_msg += "q宝爱你喔~"
    ##test_msg = MessageSegment.text(l1)
    ##await reg0.send(test_msg)
    await reg0.finish(send_msg)

@reg1.handle()
async def handle_first_receive(bot: Bot, event: Event, msg: tuple = RegexGroup()):
    send_msg = Message(MessageSegment.text("来点因子：\n"))
    send_msg = send_msg + "    " + "虚空裂隙" + "\n"
    rand_times = int(msg[1])
    l1 = random.sample(range(0, 43), rand_times)
    for i in range(0, rand_times):
        send_msg = send_msg + "    " + MessageSegment.text(Mutators[l1[i]]) + "\n"
    await reg1.finish(send_msg)

@reg2.handle()
async def handle_first_receive(bot: Bot, event: Event, msg: tuple = RegexGroup()):
    send_msg = Message(MessageSegment.text("来点因子：\n"))
    send_msg = send_msg + "    " + "风暴英雄" + "\n"
    rand_times = int(msg[1])
    l1 = random.sample(range(0, 43), rand_times)
    for i in range(0, rand_times):
        send_msg = send_msg + "    " + MessageSegment.text(Mutators[l1[i]]) + "\n"
    await reg2.finish(send_msg)

@reg3.handle()
async def handle_first_receive(bot: Bot, event: Event, msg: tuple = RegexGroup()):
    rand_times = int(msg[0])
    send_msg = Message(MessageSegment.text("来点因子：\n"))
    if rand_times == 2:
        send_msg = Message(MessageSegment.text("裂隙软"))
        await reg3.finish(send_msg)
    if rand_times == 3:
        choice = random.randint(0,2)
        if choice == 0:
            send_msg = Message(MessageSegment.text("裂隙软蜕变"))
        if choice == 1:
            send_msg = Message(MessageSegment.text("裂隙软复仇"))
        if choice == 2:
            send_msg = Message(MessageSegment.text("裂隙软部署"))
        await reg3.finish(send_msg)

@reg4.handle()
async def handle_first_receive(bot: Bot, event: Event, msg: tuple = RegexGroup()):
    send_msg = Message(MessageSegment.text("来点因子：\n"))
    send_msg = send_msg + "    " + "风暴英雄" + "\n" + "    " + "虚空裂隙" + "\n"
    rand_times = int(msg[1])
    l1 = random.sample(range(0, 43), rand_times)
    for i in range(0, rand_times):
        send_msg = send_msg + "    " + MessageSegment.text(Mutators[l1[i]]) + "\n"
    await reg2.finish(send_msg)
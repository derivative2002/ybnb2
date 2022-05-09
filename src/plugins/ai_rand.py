from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11.message import Message, MessageSegment

import random
__plugin_name__ = 'ai_rand'
__plugin_usage__ = '用法：随机AI'

printer0 = on_command("AI", priority=1, aliases={"ai"})

@printer0.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    rand_num = random.randint(0, 12)
    if rand_num == 0:
        await printer0.finish("带师机械")
    if rand_num == 1:
        await printer0.finish("果宝机甲")
    if rand_num == 2:
        await printer0.finish("LYJ炮击")
    if rand_num == 3:
        await printer0.finish("滋生腐化")
    if rand_num == 4:
        await printer0.finish("爆炸威胁")
    if rand_num == 5:
        await printer0.finish("AFK科技团")
    if rand_num == 6:
        await printer0.finish("肆虐扩散")
    if rand_num == 7:
        await printer0.finish("旧世机械团")
    if rand_num == 8:
        await printer0.finish("突鸡团")
    if rand_num == 9:
        await printer0.finish("尼玛t")
    if rand_num == 10:
        await printer0.finish("qqoo的希望")
    if rand_num == 11:
        await printer0.finish("阳宝之军")
    if rand_num == 12:
        await printer0.finish("莽咕蔽日")
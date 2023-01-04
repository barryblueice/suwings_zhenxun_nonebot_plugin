from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import Bot, Message, MessageSegment
import requests

__zx_plugin_name__ = "来点黑历史"
__plugin_usage__ = """
usage：
获取随机黑历史：来点黑历史     
获取黑历史数量：黑历史数量     
""".strip()
__plugin_des__ = "来点黑历史"
__plugin_type__ = ("一些工具",)
__plugin_cmd__ = ["来点黑历史"]
__plugin_version__ = 0.1
__plugin_author__ = "barryblueice"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["来点黑历史"],
}

hls_get = on_command("来点黑历史", block=True, priority=5)

@hls_get.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    cq = MessageSegment.image("https://papi.barryblueice.top/hls_api.php") 
    await hls_get.send(Message(cq))

hls_get_num = on_command("黑历史数量", block=True, priority=5)

@hls_get_num.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    url = 'https://papi.barryblueice.top/hls_count.php'
    resp = requests.get(url = url)
    html = resp.text
    cq = MessageSegment.text(html)
    await hls_get_num.send(Message("当前黑历史数量为："+cq))
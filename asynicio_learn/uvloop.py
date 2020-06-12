# pip install uvloop,效率堪比golang
import asyncio
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# 后面都一样
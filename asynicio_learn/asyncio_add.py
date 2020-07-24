import asyncio
import time

from threading import Thread


def start_loop(loop):
    asyncio.set_event_loop(loop)
    print("start loop", time.time())
    print(f'loop id:{loop.__dict__["_selector"]}')
    task = loop.create_task(do_some_work(8))
    loop.run_until_complete(task)


async def do_some_work(x):
    loop = asyncio.get_event_loop()
    print(f'loop id:{loop.__dict__["_selector"]}')
    print('start {}'.format(x))
    await asyncio.sleep(x)
    print('Done after {}s'.format(x))


new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()

asyncio.run_coroutine_threadsafe(do_some_work(6), new_loop)
asyncio.run_coroutine_threadsafe(do_some_work(4), new_loop)

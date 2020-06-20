"""
run2和run3不能同时调用run1
"""
import asyncio
from asyncio import Lock, Queue

queue = Queue()
lock = Lock()

async def run1():
    #使用async with lock:也可以
    await lock.acquire()
    # await asyncio.sleep(1)
    print('run1')
    lock.release()


async def run2():
    print('run2 use')
    await run1()
    print('run2 finish')



async def run3():
    print('run3 use')
    await run1()
    print('run3 finish')


if __name__ == '__main__':
    tasks = [run2(), run3()]
    asyncio.run(asyncio.wait(tasks))

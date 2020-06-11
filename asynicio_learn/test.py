import asyncio
import ctypes
import datetime
import threading


async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 2**100

    while True:
        print(datetime.datetime.now())
        print(ctypes.CDLL('libc.so.6').syscall(186))
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(0)

if __name__ == '__main__':
    asyncio.run(display_date())
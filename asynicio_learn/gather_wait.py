"""
gather可以分组
"""

import asyncio
from random import randint
from functools import partial
from time import time


async def other(i):
    print('start{0}'.format(i))
    await asyncio.sleep(abs(randint(0, 10) - i))
    print('end{0}'.format(i))
    return 'return code{0}'.format(i)


# 运行完成之后会调函数
def callBack(index, task):
    print('taskcode:{},finsh:{}'.format(index, task.result()))


async def main():
    start_time = time()
    print('main process')
    tasks1 = [asyncio.create_task(other(i)) for i in range(10)]
    for index, task in enumerate(tasks1):
        task.add_done_callback(partial(callBack, index))

    tasks2 = [asyncio.create_task(other(i)) for i in range(10)]
    for index, task in enumerate(tasks2):
        task.add_done_callback(partial(callBack, index))

    tasks1_gather = asyncio.gather(*tasks1)
    tasks2_gather = asyncio.gather(*tasks2)

    await asyncio.gather(tasks1_gather,tasks2_gather)


    print('main end,use times:{}'.format(time()-start_time))


if __name__ == '__main__':
    asyncio.run(main())

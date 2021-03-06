import asyncio
from random import randint
from functools import partial
# 使用partial可以多传参数，但参数必须放在前面

async def other(i):
    print('start{0}'.format(i))
    await asyncio.sleep(abs(randint(0,10)-i))
    print('end{0}'.format(i))
    return 'return code{0}'.format(i)


# 运行完成之后会调函数
def callBack(index, task):
    print('taskcode:{},finsh:{}'.format(index, task.result()))


async def main():
    print('main process')
    # 注意比较不同
    # demo1
    tasks = [asyncio.create_task(other(i)) for i in range(10)]
    for index, task in enumerate(tasks):
        task.add_done_callback(partial(callBack, index))
    # timeout最多等10秒，若未完成，则进入pendding,可以不
    done_tuple, pendding_tuple = await asyncio.wait(tasks, timeout=10)
    for done in done_tuple:
        print(done.result())
    # 还可以直接tasks
    # for task in tasks:
    #     print(task.result())

    # demo2
    # task = await other(0)
    # task2 = await other(1)

    print('main end')


if __name__ == '__main__':
    asyncio.run(main())

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())

import asyncio


async def other(i):
    print('start{0}'.format(i))
    await asyncio.sleep(0)
    print('end{0}'.format(i))
    return 'return code{0}'.format(i)


async def main():
    print('main process')
    # 注意比较不同
    # demo1
    tasks = [asyncio.create_task(other(i)) for i in range(5)]
    # timeout最多等一秒，若未完成，则进入pendding,可以不写
    done_tuple, pendding_tuple = await asyncio.wait(tasks, timeout=1)
    for done, in done_tuple:
        print(done.result())
    # demo2
    # task = await other(0)
    # task2 = await other(1)

    print('main end')


if __name__ == '__main__':
    asyncio.run(main())

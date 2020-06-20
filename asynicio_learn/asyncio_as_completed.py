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
    tasks = [asyncio.create_task(other(i)) for i in range(10)]
    for task in asyncio.as_completed(tasks):
        result = await task
        print('result:{}'.format(result))
    print('main end')


if __name__ == '__main__':
    asyncio.run(main())


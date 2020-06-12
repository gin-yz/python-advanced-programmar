import asyncio


async def other(i):
    print('start{0}'.format(i))
    await asyncio.sleep(0)
    print('end{0}'.format(i))
    return 'return code{0}'.format(i)


if __name__ == '__main__':
    print('main process')
    tasks = [other(i) for i in range(10)]
    done_tuple, pendding_tuple = asyncio.run(asyncio.wait(tasks, timeout=1))

    print(done_tuple)
    print('main end')

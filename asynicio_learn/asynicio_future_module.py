# future是一个底层级的api，负责循环等待
import asyncio


async def set_after(future):
    await asyncio.sleep(2)
    future.set_result('return code')


async def main():
    loop = asyncio.get_running_loop()

    future = loop.create_future()

    print(future)

    await loop.create_task(set_after(future))
    # 等待future执行完毕
    return_data = await future

    print(future)

    print(return_data)


if __name__ == '__main__':
    asyncio.run(main())

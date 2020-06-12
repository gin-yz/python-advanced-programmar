# pip install aioredis
import asyncio
import aioredis


async def execute(address, password):
    print("start")

    redis = await aioredis.create_redis(address, db=1, password=password)

    await redis.hmset_dict('car', key1=1, key2=2, key3=3)

    result = await redis.hgetall('car', encoding='utf-8')

    print(result)
    # 关闭io
    redis.close()
    await redis.wait_closed()

    print("end")


if __name__ == '__main__':
    task_list = [
        execute('redis://127.0.0.1:6379', '123456'),
        execute('XxxxxxxxxXXXxXXX', '123456')
    ]
    asyncio.run(asyncio.wait(task_list))

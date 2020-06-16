import aiohttp
import asyncio


async def fetch(session, url):
    print("发送请求:", url)
    async with session.get(url, verify_ssl=False) as response:
        text = await response.text()
        print("得到[%s]结果:" % url, len(text))


async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            'https://www.chiphell.com/',
            'http://www.baidu.com',
            'http://www.pythonav.com'
        ]

        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]
        await asyncio.wait(tasks)

        # await fetch(session,url_list[0])
        # await fetch(session,url_list[1])
        # await fetch(session,url_list[2])


if __name__ == '__main__':
    asyncio.run(main())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())

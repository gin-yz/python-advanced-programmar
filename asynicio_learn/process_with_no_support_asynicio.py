"""
若程序不支持携程，则使用线程的方式辅助
"""

import asyncio
import requests
import time

async def download_something(url):
    print("开始下载:%s" % url)
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None,requests.get,url)
    response = await future
    print("下载结束:%s" % response)


async def main():
    url_list = [
        'https://www.chiphell.com/',
        'https://www.baidu.com',
        'https://www.douban.com'
    ]*2**10
    tasks = [asyncio.create_task(download_something(url)) for url in url_list]
    done, pedding = await asyncio.wait(tasks)
    print(done, pedding)


if __name__ == '__main__':
    asyncio.run(main())

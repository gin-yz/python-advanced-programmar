import asyncio


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()


async def main():
    tasks = [asyncio.create_task(tcp_echo_client('Hello!:{}'.format(i))) for i in range(20)]

    done, pedding = await asyncio.wait(tasks)

    for do in done:
        print(do.result())


if __name__ == '__main__':
    asyncio.run(main())

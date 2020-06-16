# pip install aiomysql

import asyncio
import aiomysql


async def execute(host, password):
   print('start')

   conn = await aiomysql.connect(host=host,port=3306,user='root',password=password,db='test')

   cur = await conn.cursor()

   await cur.execute("SELECT idnew_table1 FROM new_table1")

   result = await cur.fetchall()

   print(result)

   await cur.close()
   conn.close()

   print("end")

if __name__ == '__main__':
    task_list=[
        execute('127.0.0.1','123456')
    ]

    asyncio.run(asyncio.wait(task_list))
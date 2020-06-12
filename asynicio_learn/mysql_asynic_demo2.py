# pip install aiomysql

import asyncio
import aiomysql


async def execute(sql_str):
   print('start')

   conn = await aiomysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',db='test')

   cur = await conn.cursor()

   await cur.execute(sql_str)

   result = await cur.fetchall()

   print(result)

   await cur.close()
   conn.close()

   print("end")

if __name__ == '__main__':
    task_list=[
        execute("SELECT idnew_table1 FROM new_table1"),
        execute("SELECT * FROM new_table1"),
    ]
    print(task_list)
    asyncio.run(asyncio.wait(task_list))
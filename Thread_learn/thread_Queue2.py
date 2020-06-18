"""
Queue在调用时已经是线程安全的，也就是说不同线程只能互斥的访问
"""
import os
import time
from queue import Queue
import threading

q = Queue()


def consumer(name):
    while True:  # 死循环表示消费者在理想状态下无线工作
        time.sleep(1)  # 把睡眠关闭 表示消费者的消费速度大于生产者生产速度
        print(name, q.get())  # 从管道（队列）中取出商品


def producer():
    i = 0
    while True:
        time.sleep(1)  # 假装一秒钟生产一件商品
        q.put(i)  # 用时间戳来当做生产者生产的商品
        i += 1


if __name__ == '__main__':
    t_pro = threading.Thread(target=producer)
    t_con = threading.Thread(target=consumer, args=(1,))
    t_con2 = threading.Thread(target=consumer, args=(2,))
    t_pro.start()
    t_con.start()
    t_con2.start()

    print(os.getpid())

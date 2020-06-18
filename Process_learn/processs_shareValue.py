"""
进程声明全局变量后不能共享，线程可以。但是使用manage中的方法可以共享全局变量，有list还有dic以及多种数据结构
"""

from multiprocessing import Manager, Process


def add_data(s_dict, key, value):
    s_dict[key] = value


if __name__ == '__main__':
    share_dict = Manager().dict()
    process1 = Process(target=add_data,args=(share_dict,'cjs','woshicjs',))
    process2 = Process(target=add_data, args=(share_dict, 'cys', 'woshicys',))
    process1.start()
    process2.start()
    process1.join()
    process2.join()

    print(share_dict)
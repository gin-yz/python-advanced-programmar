import os
from multiprocessing import Process


def run_test(name1, name2, name3, **kwargs):
    print('子进程:%s' % os.getpid())
    print(locals())
    print('子进程终止')


if __name__ == '__main__':
    print('主进程:%s' % os.getpid())
    # 元祖里面一个参数，带上“，”
    p = Process(target=run_test, args=(1, 2, 'test',), kwargs={'name4': 4, 'name5': 5})

    p.start()

    print('子进程pid：%s，子进程状态：%s'%(p.pid,p.is_alive()))
    # 主进程等待子进程,timeout超时时间
    p.join(timeout=100)

    print('主进程终止')

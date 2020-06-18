
import os
import time
# 紫禁城返回0，赴京城返回紫禁城pid
pid = os.fork()

print('hello 金箔')

if pid ==0:
    print('我是子进程，我的pid是{},我的父进程pid为{}'.format(os.getpid(),os.getppid()))
else:
    print('我是父进程，我的pid为{},我的子进程pid为{}'.format(os.getpid(),pid))

time.sleep(2)
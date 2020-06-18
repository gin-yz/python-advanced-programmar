# apply(同步，阻塞),apply_async(异步,非阻塞)
# 进程池满了之后要等待其他进程执行完毕
import os
from multiprocessing import Pool,cpu_count
from time import sleep


def func(num):
    print('子进程:%s' % os.getpid())
    print('process %s start' % num)
    sleep(1)
    print('process %s end' % num)
    return num

def func2(num):
    print('子进程:%s' % os.getpid())
    print('process %s start' % num)
    sleep(num)
    print('process %s end' % num)
    return num

if __name__ == '__main__':
    result_list =[]
    pool = Pool(processes=3)
    for i in range(10):
        result_list.append(pool.apply_async(func=func,args=(i,)))

    #close()并不是关闭进程池，而是不再接受新进程
    pool.close()

    pool.join()
    for i in result_list:
        print(i.successful(),i.ready(),i.get())

    #也可以使用imap直接返回return内容,imap会等待结果完成,按照顺序输出
    pool2 = Pool(processes=cpu_count())
    for result in pool2.imap(func2,(1,7,3)):
        print(result)

    #使用imap直接返回return内容,imap会等待结果完成,谁先完成谁先输出
    pool3 = Pool(processes=cpu_count())
    for result in pool3.imap_unordered(func2,(1,7,3)):
        print(result)



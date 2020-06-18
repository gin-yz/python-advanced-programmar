"""
pipe为简化版的quque，只能应用于两个进程的通信
"""

from multiprocessing import Process,Pipe

def send(send_pipe):
    send_pipe.send('hello')

def recive(recv_pipe):
    print(recv_pipe.recv())

if __name__ == '__main__':

    recv_pipe,send_pipe = Pipe()

    send_process = Process(target=send,args=(send_pipe,))

    recv_process = Process(target=recive,args=(recv_pipe,))

    send_process.start()
    recv_process.start()
    send_process.join()
    recv_process.join()
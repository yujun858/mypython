from threading import Thread
import os
from multiprocessing import Process

def work():
    print(os.getpid()) #得到父进程id
if __name__ == "__main__":
    t1 = Thread(target=work)
    t2 = Thread(target=work)
    t1.start()
    t2.start()
    print(os.getpid())
    p1 = Process(target=work)
    p2 = Process(target=work)
    p1.start()
    p2.start()
    print(os.getpid())
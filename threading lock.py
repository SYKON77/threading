from threading import *
import threading

x = 0

def thread_task(lock):
    global x
    for i in range(10):
        lock.acquire()
        x += 1
        print(x)
        lock.release()

def main_task():
    lock = threading.Lock()
    
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

main_task()

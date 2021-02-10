from threading import *
import threading

class one(threading.Thread):
    def run(self):
        i = 5
        while i <= 10:
            i = i + 1
            print (i)
            threadlock.acquire()
            threadlock.release()
            

class two(threading.Thread):
    def run(self):
        j = 1
        while j <= 5:
            j = j + 1
            print (j)

threadlock = threading.lock()

t1 = one()
t2 = two()

t1.start()
t2.start()

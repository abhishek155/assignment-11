# ques 1
import threading
from threading import Thread
import time
class mythread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        time.sleep(5)
        print("value send", self.h)

thread1 = mythread(1)
thread1.start()

## ques 2
import threading
import time
from threading import Thread
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        print("no. is", self.h)
for i in range(10):
    thread1 = Mythread(i)
    thread1.start()
    time.sleep(1)

### ques 3
import threading
import time


class Mythread(threading.Thread):
    def __init__(self, value):
        threading.Thread.__init__(self)
        self.v = value

    def run(self):
        h = [2, 4, 6, 8, 10]
        for i in range(0, 5):
            print(self.v[i])
            time.sleep(h[i])


thread1 = Mythread([1, 2, 3, 4, 5])
thread1.start()

#### ques 4
import threading
import math
class Mythread(threading.Thread):
    def __init__(self,value):
        threading.Thread.__init__(self)
        self.v=value

    def run(self):
        print(math.factorial(self.v))


thread1=Mythread(6)
thread1.start()
import threading
import queue

class A(threading.Thread):
    def __init__(self):
        #init the threading
        threading.Thread.__init__(self)
    def run(self):
        #what will do in next
        for i in range(10):
            print("I am threading A")
class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(10):
            print("I am threading B")

t1 = A()
t1.start()
t2 = B()
t2.start()
import threading
import time
from time import *

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID= threadID
        self.name=name
        self.counter=counter
    def run(self):
        print("Starting Thread..."+self.name +"\n")
        print(self.name,self.counter,5)
        print("Exiting"+ self.name +"\n")
        
def ptiny_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print("%s: %s %s" % (threadName,time.ctime(time.time()),counter) + "\n")
        counter-=1
        

thread1= myThread(1,"Thread-1",1)
thread2= myThread(2,"Thread-2",2)


thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting the Main Thread")
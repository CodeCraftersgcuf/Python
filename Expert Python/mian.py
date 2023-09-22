#import inspect 
#import random
#print(inspect.getsource(random))

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        rv=func()
        total=time.time() - start
        print("Time: ", total)
        return rv
    
    return wrapper

@timer
def test():
    for i in range(100000):
        pass

test()
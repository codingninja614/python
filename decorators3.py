from time import time
def performance(fn):
    def wrapper(*args,**kwargs):
        t1=time()
        result=fn(*args,**kwargs)
        t2=time()
        time_taken=str(t2-t1)
        print("TOOK:" + time_taken +  "units of time!")
        return result
    return wrapper

@performance
def timer():
    for i in range(1000000):
        i**2

timer()

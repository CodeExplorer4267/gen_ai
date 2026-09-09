#GIL in multiprocessing 
from multiprocessing import Process
import time

def count():
    print(f" started counting...")
    x=0
        #this is a CPU intensive task
    for _ in range(100_000_000):
        x+=1
    print(f"finished counting...")

#if we don't write this . this wil give us an error.Only in multiprocessing
if __name__=="__main__":
    p1=Process(target=count)
    p2=Process(target=count)
    start=time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end=time.time()
    print(f"Total time taken:{end-start:.2f}")


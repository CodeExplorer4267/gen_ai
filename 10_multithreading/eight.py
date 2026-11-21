#GIL
from multiprocessing import Process
import time

def count():
    print(f"started counting...")
    x=0
    #this is a CPU intensive task
    for _ in range(100_000_000):
        x+=1
    print(f" finished counting...")

if __name__ == "__main__":
    start=time.time()
    processes=[Process(target=count) for _ in range(2)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    end=time.time()
    print(f"Total time {end-start:.2f} seconds")
    
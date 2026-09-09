#GIL
import threading
import time

def count():
    print(f"${threading.current_thread().name} started counting...")
    x=0
    #this is a CPU intensive task
    for _ in range(100_000_000):
        x+=1
    print(f"${threading.current_thread().name} finished counting...")

thread1=threading.Thread(target=count,name="Rupam")
thread2=threading.Thread(target=count,name="Rupam2")

start=time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end=time.time()

print(f"Total time {end-start:.2f} seconds")

#For CPU-intensive Python code, using multiple threads doesn't provide true parallel execution of Python bytecode because of the GIL.


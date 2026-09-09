#Create two threads to perform two different tasks.this is concurrency-> multithreading
import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking ${i} order")
        time.sleep(1)

def make_order():
    for i in range(1,4):
        print(f"Making ${i} order")
        time.sleep(3)

#create threads -> here it is switching the context
order_thread=threading.Thread(target=take_orders)
make_thread=threading.Thread(target=make_order)

order_thread.start()
make_thread.start()

# join() means: Wait until this thread finishes.So the main program will not continue to:print("All orders are taken") until both threads have completed.
order_thread.join()
make_thread.join()

print(f"All orders are taken")
import time
from threading import Thread

def count(n):
    while n > 0:
        n -= 1

def thread_test():
    n = 10000000
    t1 = Thread(target=count, args=(n//2,))
    t2 = Thread(target=count, args=(n//2,))

    start_time = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.time()

    return end_time - start_time

iterations = 10
total_time = 0
for _ in range(iterations):
    total_time += thread_test()

average_time = total_time / iterations
print(f"Average time taken with multithreading over {iterations} iterations: {average_time} seconds")

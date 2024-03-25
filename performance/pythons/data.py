import time
import random

iterations = 10
total_time = 0
for _ in range(iterations):
    data = [random.randint(0, 1000000) for _ in range(100000)]
    start_time = time.time()
    sorted_data = sorted(data)
    end_time = time.time()
    total_time += (end_time - start_time)

average_time = total_time / iterations
print(f"Average time taken to sort 100,000 integers over {iterations} iterations: {average_time} seconds")

import time

import rust_extension

iterations = 10
total_time = 0
for _ in range(iterations):
    start_time = time.time()
    rust_extension.fibonacci(30)
    end_time = time.time()
    total_time += (end_time - start_time)

average_time = total_time / iterations
print(f"Average time taken over {iterations} iterations: {average_time} seconds")

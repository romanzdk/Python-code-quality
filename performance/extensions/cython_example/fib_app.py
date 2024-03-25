import time
from distutils.core import setup

from Cython.Build import cythonize
# Assuming fib.pyx is compiled to a module named fib
from fib import fibonacci

iterations = 10
total_time = 0
for _ in range(iterations):
    start_time = time.time()
    fibonacci(30)  # Calling the Cython version of the fib function
    end_time = time.time()
    total_time += (end_time - start_time)

average_time = total_time / iterations
print(f"Average time taken over {iterations} iterations: {average_time} seconds")

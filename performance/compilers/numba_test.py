import time

import numpy as np
from numba import jit

# Mandelbrot set parameters
width, height = 800, 800
max_iter = 50

def mandelbrot_python(x, y, max_iter):
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iter):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    return max_iter

def mandelbrot_set_python(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return [[mandelbrot_python(x, y, max_iter) for x in r1] for y in r2]

@jit
def mandelbrot_numba(x, y, max_iter):
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iter):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    return max_iter

@jit
def mandelbrot_set_numba(xmin, xmax, ymin, ymax, width, height, max_iter):
    result = np.zeros((height, width), dtype=np.int64)
    for i in range(height):
        for j in range(width):
            result[i, j] = mandelbrot_numba(xmin + j*(xmax-xmin)/width, ymin + i*(ymax-ymin)/height, max_iter)
    return result

# Benchmarking
def benchmark_mandelbrot(func, xmin, xmax, ymin, ymax, width, height, max_iter):
    start_time = time.time()
    result = func(xmin, xmax, ymin, ymax, width, height, max_iter)
    return time.time() - start_time

# Running the benchmarks
python_time = benchmark_mandelbrot(mandelbrot_set_python, -2.0, 1.0, -1.5, 1.5, width, height, max_iter)
numba_time = benchmark_mandelbrot(mandelbrot_set_numba, -2.0, 1.0, -1.5, 1.5, width, height, max_iter)

print(f"Python: {python_time:.2f} seconds")
print(f"Numba: {numba_time:.2f} seconds")

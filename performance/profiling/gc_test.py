
import gc
import os
import tracemalloc

import psutil


def get_psutil():
	process = psutil.Process(os.getpid())
	print(f"[psutil] {process.memory_info().rss / 1024 ** 2}MB")

def get_tracemalloc():
	current, _ = tracemalloc.get_traced_memory()
	print(f"[tracemalloc] {current / 10**6}MB")

tracemalloc.start()

print('[0] "Empty" program')
get_psutil()
get_tracemalloc()

print('\n[1] Large object allocated')
large_list = [list(range(1_000)) for _ in range(10_000)]
get_psutil()
get_tracemalloc()
input('Waiting for input')

print('\n[2] Object deleted')
del large_list
get_psutil()
get_tracemalloc()
input('Waiting for input')

print("\n[3] Object gc'ed")
gc.collect()
get_psutil()
get_tracemalloc()
input('Waiting for input')
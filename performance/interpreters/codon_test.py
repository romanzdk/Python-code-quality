#https://thenewstack.io/codon-is-a-faster-python-compiler-for-some-workloads/
from time import time


def fib(n):
	return n if n < 2 else fib(n - 1) + fib(n - 2)
 
t0 = time()
ans = fib(40)
t1 = time()
print(f'Computed fib(40) = {ans} in {t1 - t0} seconds.')
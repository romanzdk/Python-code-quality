import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def compute_primes(limit):
    primes = []
    for number in range(limit):
        if is_prime(number):
            primes.append(number)
    return primes

iterations = 10
total_time = 0
for _ in range(iterations):
    start_time = time.time()
    compute_primes(100_000)
    end_time = time.time()
    total_time += (end_time - start_time)

average_time = total_time / iterations
print(f"Average time taken to compute primes up to 100_000 over {iterations} iterations: {average_time} seconds")

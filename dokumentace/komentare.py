def debug(func):
    """
    A decorator for debugging that prints the name of the function and its return values
    each time it is called. Useful for complex debugging when we need
    to track how data is transformed through different functions.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Calls the original function
        print(f"{func.__name__} returned {result}")  # Prints information about the call
        return result
    return wrapper

@debug  # Applying the debug decorator to the function below
def multiply(x, y):
    return x * y



def find_primes_in_range(start, end):
    """
    Returns a list of prime numbers in a given range.
    Uses the Sieve of Eratosthenes for efficient prime number searching.
    This algorithm is efficient for large ranges, but its memory
    consumption can be high for very large 'end' values.
    """
    sieve = [True] * (end + 1)  # Initializes the sieve with truth values
    primes = []
    for current_number in range(2, end + 1):
        if sieve[current_number]:  # If the number is still marked as a prime
            primes.append(current_number)  # Adds the prime number to the list
            # Marks multiples of the number as non-prime
            for multiple in range(current_number*2, end + 1, current_number):
                sieve[multiple] = False
    return primes[start:end]  # Returns the primes in the requested range


def divide_some_special_thing(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        # Because of company policy X123 we return x in case y is zero
        print("Warning: Attempt to divide by zero.")
        return x

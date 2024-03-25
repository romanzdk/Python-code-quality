def f(a, b):
    if a:
        for i in range(b):
            if b:
                return 1


def g(a, b):
    if a:
        return 1


def check_number(num):
    if num > 0:
        return "Positive"
    elif num == 0:
        return "Zero"
    else:
        return "Negative"


def calculate_area(length, width):
    area = length * width
    return area


def greet(name):
    print(f"Hello, {name}!")


def example_function(x):
    if x > 0:
        for i in range(x):
            if i % 2 == 0:
                print(i)


def complex_function(data, threshold):
    def helper(subset):
        if len(subset) == 1:
            return subset[0] > threshold
        else:
            mid = len(subset) // 2
            left = helper(subset[:mid])
            right = helper(subset[mid:])
            return left and right

    if not data:
        return False

    result = 0
    for i in range(len(data)):
        for j in range(i, len(data)):
            if i != j and data[i] == data[j]:
                result += 1
            elif helper(data[i:j+1]):
                result += data[i] + data[j]
            else:
                for k in range(i, j+1):
                    if data[k] > threshold:
                        result += 1
                    else:
                        for l in range(k+1, len(data)):
                            if data[l] % data[k] == 0:
                                result -= 1
                            else:
                                result += 2
    return result


def sum_of_primes(max_val):
    total = 0
    for i in range(1, max_val + 1):  # Iterate from 1 to max_val inclusive
        if i > 1:  # Prime numbers are greater than 1
            for j in range(2, i):
                if (i % j) == 0:
                    break  # Not a prime number
            else:
                total += i  # Add prime number to total
    return total


def get_words(number):
    match number:
        case 1:
            return "one"
        case 2:
            return "a couple"
        case 3:
            return "a few"
        case _:
            return "lots"


class Animal:
    pass


class Mammal(Animal):
    pass


class Dog(Mammal):
    pass


print(Dog.mro())
print(len(Dog.mro()))

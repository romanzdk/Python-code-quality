import random
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def main():
    arr = [random.randint(0, 10_000) for p in range(0, 1000)]
    
    start = time.time()
    bubble_sort(arr)
    print(f"Bubble sort = {time.time()-start}")
    
    start = time.time()
    quicksort(arr)
    print(f"Quick sort = {time.time()-start}")

if __name__ == '__main__':
    main()

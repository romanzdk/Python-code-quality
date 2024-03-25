@profile
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

@profile
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    print("Sorted array with bubble sort: ", arr)

    arr = [64, 34, 25, 12, 22, 11, 90]
    arr = quicksort(arr)
    print("Sorted array with quicksort: ", arr)

if __name__ == '__main__':
    main()

from Find_Time import find_time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swaps = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps = True
 
        if not swaps:
            break
    return arr

test_arr = [100, 0, -123, 2, -5, 5, 4, 234, 2, 34, -34, 43, 2, -120, 1, 2, 2, 1, 1, 2, 3, 4, -59]

assert bubble_sort(test_arr) == sorted(test_arr)
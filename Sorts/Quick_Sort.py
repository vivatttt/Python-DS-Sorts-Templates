import random

def pivot_first_el(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [el for el in arr[1:] if el < pivot]
    right = [el for el in arr[1:] if el >= pivot]

    return pivot_first_el(left) + [pivot] + pivot_first_el(right)

def pivot_last_el(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [el for el in arr[:-1] if el < pivot]
    right = [el for el in arr[:-1] if el >= pivot]

    return pivot_last_el(left) + [pivot] + pivot_last_el(right)

def pivot_random_el(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)

    left, middle, right = [], [], []
    for el in arr:
        if el < pivot:
            left.append(el)
        elif el > pivot:
            right.append(el)
        else:
            middle.append(el)
    return pivot_random_el(left) + middle + pivot_random_el(right) 

def pivot_random_without_extra_space(arr, l, r):
    if l >= r:
        return arr
    
    pivot = random.choice(arr[l:r + 1])

    i, j = l, r
    while i - j <= 0:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

            pivot_random_without_extra_space(arr, l, j)
            pivot_random_without_extra_space(arr, i, r)


test_arr = [-1, -100, -1, 2, 0, 20, 15, 10, 4, -19]

assert pivot_first_el(test_arr) == sorted(test_arr)
assert pivot_last_el(test_arr) == sorted(test_arr)
assert pivot_random_el(test_arr) == sorted(test_arr)
test_copy_arr = test_arr.copy()
pivot_random_without_extra_space(test_copy_arr, 0, len(test_copy_arr) - 1)
assert test_copy_arr == sorted(test_arr)
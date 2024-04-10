from random import randint
def merge(left_arr, right_arr):
    # функция объединения двух отсортированных списков

    res = []
    left_ind = right_ind = 0
    len_l, len_r = len(left_arr), len(right_arr)

    # ставим указатели на начала списков и заносим в результирующий массив наименьший из эл-тов, на которые указывают указатели
    while left_ind < len_l and right_ind < len_r:

        if left_arr[left_ind] > right_arr[right_ind]:
            res.append(right_arr[right_ind])
            right_ind += 1
        else:
            res.append(left_arr[left_ind])
            left_ind += 1
    
    if left_ind < len_l:
        res += left_arr[left_ind:]
    if right_ind < len_r:
        res += right_arr[right_ind:]
    
    return res

# функция, которая рекурсивно разделяет список на списки по одному элементу
# затем, с помощью функции merge объединяет их в остортированные списки, которые в свою очердь объединяются в большой отсортированный массив
def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    
    m = len(arr) // 2

    left_arr = merge_sort(arr[:m])
    right_arr = merge_sort(arr[m:])

    return merge(left_arr, right_arr)


test_arr = [1, -12, 1, 2, 2324, -234, 2, 1, 46, -6, 0, 0, 12]
test_arr_random = [randint(-1000, 1000) for _ in range(1000)]
assert merge_sort(test_arr_random) == sorted(test_arr_random)



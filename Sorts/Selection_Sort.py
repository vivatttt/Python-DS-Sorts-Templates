def selection_sort(arr):
    '''
    Выбираем наименьший элемент в массиве arr[i:] и меняем местами i и min_i
    '''
    n = len(arr)

    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]

test_arr = [1, -20, -10, 1, 2, 3, -2, -3, 2, 12, 11, 12, 19234]
test_arr_copy = test_arr.copy()
selection_sort(test_arr_copy)
assert test_arr_copy == sorted(test_arr)

import random

# смысл в том, что слева - отсортированный массив
# первый неотсортированный элемент и перемещаем его на свое место в левом массиве
# делаем это путем сдвига всех элементов отсортированной части массива до тех пор, пока не освободим место для нашего элемента
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):

        item_to_insert = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > item_to_insert:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = item_to_insert


test_arr = [random.randint(-1000, 1000) for _ in range(1000)]

test_arr_copy = test_arr.copy()
insertion_sort(test_arr_copy)

assert test_arr_copy == sorted(test_arr)

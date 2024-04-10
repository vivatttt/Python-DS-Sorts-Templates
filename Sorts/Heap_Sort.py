from heapq import heappush, heappop

def heapify(arr, root_ind, heap_size):
    maxx = root_ind
    # задача поднять наибольший элемент
    # берем правого и левого потомка текущего корня и находим максимальный

    left = root_ind * 2 + 1
    right = root_ind * 2 + 2

    if left < heap_size and arr[left] > arr[maxx]:
        maxx = left
    
    if right < heap_size and arr[right] > arr[maxx]:
        maxx = right
    
    if maxx != root_ind:
        # если найденный максимальныый элемент - потомок, вызываем
        arr[root_ind], arr[maxx] = arr[maxx], arr[root_ind]
        # применяем операцию heapify к новому корню, чтобы убедиться, что он наибольший
        heapify(arr, maxx, heap_size)
    
def heap_sort(arr):
    n = len(arr)

    # строим пирамиду по правилу:
    # arr[i] >= arr[2i + 1] and arr[i] >= arr[2i + 2]
    #       5
    #    6    3
    #  10 1  4  7
    # ->
    #       5
    #    6    3
    #  |10| 1  4  7
    # ->
    #       5
    #  |10|   3
    #  6  1  4  7

    '''
    Берем узлы по порядку снизу и "поднимаем" одного ребенка, если он больше текущего узла. 
    '''

    for i in range(n, -1, -1):
        heapify(arr, i, n)
    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

def heap_sort_using_heapq(arr):
    heap = []

    # формируем мин кучу
    for el in arr:
        heappush(heap, el)
    
    res = []
    
    # последовательно достаем из кучи первый (минимальный) элемент и добавляем его в результирующий массив
    while heap:
        cur_max = heappop(heap)
        res.append(cur_max)
        print(res)

    return res

test_arr = [5, 6, 3, 10, 1, 4, 7]
test_arr_copy = test_arr.copy()
heap_sort(test_arr_copy)

assert test_arr_copy == sorted(test_arr)
assert heap_sort_using_heapq(test_arr) == sorted(test_arr)  



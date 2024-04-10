class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def insert(self, el):

        self.size += 1
        # добавляем элемент в конец кучи
        self.heap.append(el)
        # поднимаем элемент на свое место
        self.bubble_up(self.size - 1)
    def extract_min(self):
        if self.size == 0:
            return 
        
        minn = self.heap[0]
        # ставим последний элемент из кучи в начало
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        # опускаем элемент на свое место
        self.size -= 1
        self.bubble_down(0)
        
        return minn

    def bubble_up(self, ind):
        parent = ind // 2

        if ind < 1:
            return
        # если текущий элемент меньше родителя, меняем их местами
        if self.heap[ind] < self.heap[parent]:

            self.heap[parent], self.heap[ind] = self.heap[ind], self.heap[parent] 
            # вызываем функцию подъема уже от родительского элемента
            # для того, чтобы проверить, встал ли он на свое место (его родитель меньше его)
            self.bubble_up(parent)
    
    def bubble_down(self, ind):
        left = 2 * ind + 1
        right = 2 * ind + 2

        smallest = ind
    
        if left < self.size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != ind:
            # ребенок меньше родителя (текущего узла) => поднимаем его

            self.heap[smallest], self.heap[ind] = self.heap[ind], self.heap[smallest]
            self.bubble_down(smallest)

    def print(self):
        print(*self.heap)

min_heap = MinHeap()
min_heap.insert(5)
min_heap.print()
min_heap.insert(6)
min_heap.print()
min_heap.insert(2)
min_heap.print()
min_heap.insert(9)
min_heap.print()
min_heap.insert(3)
min_heap.print()


print(min_heap.extract_min()) 
print(min_heap.extract_min()) 
print(min_heap.extract_min()) 
print(min_heap.extract_min())
print(min_heap.extract_min())

# для создания максимальной кучи, просто передаем -el
# а когда извлекаем очередной элемент, берем его со знаком минус

    
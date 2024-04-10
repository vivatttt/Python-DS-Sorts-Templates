class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.dictt = dict()
        self.cur_size = 0

    def get(self, key: int) -> int:
        if key not in self.dictt.keys():
            return -1
        else:
            cur_node = self.dictt[key]
            if self.cur_size == 1 or cur_node == self.head: # если нужно изменить единственный добавленный элемент или стоящий в начале
                cur_node.val = self.dictt[key].val
            elif self.cur_size == 2:
                # жесткий каламбур для двух узлов (меняем сначала направление ссылаемости, потом голову и хвост местами)
                self.tail.next = self.head
                self.head.prev = self.tail

                self.head, self.tail = self.tail, self.head
                self.head.prev = None
                self.tail.next = None
            elif cur_node.next == None:
                cur_node.prev.next = None
                self.tail = cur_node.prev

                cur_node.next = self.head
                self.head.prev = cur_node
                cur_node.prev = None
                
                self.head = cur_node
            else:
                # связываем два узла, между которыми удаляли узел
                cur_node.prev.next = cur_node.next 
                cur_node.next.prev = cur_node.prev

                # ставим узел в начало
                
                cur_node.next = self.head
                self.head.prev = cur_node
                cur_node.prev = None
                self.head = cur_node
            return self.dictt[key].val

    def put(self, key: int, value: int) -> None:
        # имеем двухсвязный список, каждый узел которого лежит в словаре
        # наличие словаря позволяет функции get() выполняться за константное время
        # а наличие двухсвязного списка упрощает работу с перестановкой элемента в начало (двухсвязность позволяет связывать узлы, где был вынут узел)
        if key not in self.dictt.keys(): # если еще нет такого узла
            # создаем новый узел и помещаем в начало
            new_node = Node(value, key)
            if self.cur_size == 0:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            
            self.cur_size += 1
            self.dictt[key] = new_node
        else:
           
            cur_node = self.dictt[key]
            if self.cur_size == 1 or cur_node == self.head: # если нужно изменить единственный добавленный элемент или стоящий в начале
                cur_node.val = value
            elif self.cur_size == 2:
                # жесткий каламбур для двух узлов (меняем сначала направление ссылаемости, потом голову и хвост местами)
                self.tail.next = self.head
                self.head.prev = self.tail

                self.head, self.tail = self.tail, self.head
                self.head.prev = None
                self.tail.next = None

                self.head.val = value
            elif cur_node.next == None:
                cur_node.prev.next = None
                self.tail = cur_node.prev

                cur_node.next = self.head
                self.head.prev = cur_node
                cur_node.prev = None
                
                self.head = cur_node
                
                self.head.val = value
            else:
                # связываем два узла, между которыми удаляли узел
                cur_node.prev.next = cur_node.next 
                cur_node.next.prev = cur_node.prev

                # ставим узел в начало
                
                cur_node.next = self.head
                self.head.prev = cur_node
                cur_node.prev = None
                self.head = cur_node
                self.head.val = value

        # если превысили вместимость, удаляем последний эл-т
        if self.cur_size > self.capacity:
            del self.dictt[self.tail.key] # удаляем элемент из словаря
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.cur_size -= 1



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
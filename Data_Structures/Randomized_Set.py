from random import choice

class RandomizedSet:
    def __init__(self):
        self.dictt = {}
        self.arr = []
        
    def insert(self, val: int) -> bool:
        if val in self.dictt.keys():
            return False
        self.arr.append(val)
        self.dictt[val] = len(self.arr) - 1
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.dictt.keys():
            return False
        # не можем просто удалить элемент из массива, так как собьются все индексы последующих элементов
        self.dictt[self.arr[-1]] = self.dictt[val]
        self.arr[self.dictt[val]] = self.arr[-1]
        self.arr.pop()
        del self.dictt[val]
        
        return True

    def getRandom(self) -> int:
        return choice(self.arr)

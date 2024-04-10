class HashSet:
    def __init__(self, capacity = 10**9):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
    def hashit(self, item):
        return abs(hash(item)) % self.capacity
    def add(self, el):
        hash_value = self.hashit(el)
        if el not in self.buckets[hash_value]:
            self.buckets[hash_value].append(el)
    def remove(self, el):
        hash_value = self.hashit(el)
        if el in self.buckets[hash_value]:
            self.buckets[hash_value].remove(el)
    def contains(self, el):
        hash_value = self.hashit(el)
        return el in self.buckets[hash_value]
            
    def size(self):
        count = 0
        for bucket in self.buckets:
            count += len(bucket)
        return count

    def print(self):
        r = []
        for bucket in self.buckets:
            r += bucket
        print('{' + ', '.join(map(str, r)) + '}') 

myset = HashSet(100)

myset.add(10)
myset.add(10)
myset.add(20)
myset.add(-2304)
myset.add('sister')
myset.add((1, 2))
myset.remove(10)
myset.print()




    

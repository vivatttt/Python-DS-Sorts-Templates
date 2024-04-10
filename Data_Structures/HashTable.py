class HashTable:
    def __init__(self, capacity=109):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
    def hashit(self, key):
        return abs(hash(key)) % self.capacity
    
    def insert(self, key, value):
        hash_value = self.hashit(key)

        for i, pair in enumerate(self.buckets[hash_value]):
            if key == pair[0]:
                # если ключ уже в мапе, обновляем значение по этому ключу
                self.buckets[hash_value][i] = value
                return 
        self.buckets[hash_value].append((key, value))
    def get(self, key):
        hash_value = self.hashit(key)

        for cur_key, cur_val in self.buckets[hash_value]:
            if key == cur_key:
                return cur_val
        raise KeyError
    def remove(self, key):
        hash_value = self.hashit(key)
        for i, pair in enumerate(self.buckets[hash_value]):
            if pair[0] == key:
                del self.buckets[hash_value][i]
                return
        raise KeyError


    def contains(self, key):
        hash_value = self.hashit(key)

        for cur_key, _ in self.buckets[hash_value]:
            if cur_key == key:
                return True
        return False
    def keys(self):
        r = []
        for el in self.buckets:
            for key, val in el:
                r.append(key)
        return r
    def values(self):
        r = []
        for el in self.buckets:
            for key, val in el:
                r.append(val)
        return r


hash_table = HashTable()

hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("orange", 30)


print(hash_table.get("apple"))   
print(hash_table.get("banana"))  


print(hash_table.contains("orange"))  
print(hash_table.contains("grapes"))   
hash_table.remove("banana")
print(hash_table.contains("banana"))  

print(hash_table.keys())
print(hash_table.values())
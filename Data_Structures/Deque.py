class Deque:
    def __init__(self):
        self.items = []

    def push(self, el):
        self.items.append(el)

    def pop(self):
        if not self.items:
            return 
        return self.items.pop()
    
    def pushleft(self, el):
        self.items.insert(0, el)

    def popleft(self):
        if not self.items:
            return
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def print(self):
        for el in self.items:
            print(f'{el} -> ', end='')


dq = Deque()

dq.push(1)
dq.pushleft(2)
dq.pop()
dq.push(12)
dq.push(14)
dq.popleft()
dq.print()
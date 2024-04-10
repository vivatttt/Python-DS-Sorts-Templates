class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, el):
        self.stack.append(el)
    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def print(self):
        for el in self.stack:
            print(f'{el} -> ', end='')
        

stack = Stack()

stack.push(1)
stack.push(10)
stack.pop()
stack.push(12)
stack.print()




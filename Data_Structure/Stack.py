class Stack:
    def __init__(self):
        self.item = []
    def push(self,data):
        self.item.append(data)
    def pop(self):
        return self.item.pop()
    def size(self):
        return len(self.item)
    
S=Stack()
S.push(10)
S.push(20)
S.push(30)
print(S.item)
print(S.pop())

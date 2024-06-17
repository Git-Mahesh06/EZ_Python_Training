class Queue:
    def __init__(self):
        self.item=[]
    def push(self,data):
        self.item.append(data)
    def remove(self):
        return self.item.pop(0)
    def size(self):
        return len(self.item)
q=Queue()
n=int(input("Enter the number "))
for _ in range(1,n+1):
    i=int(input())
    q.push(i)
print(q.item)
print(q.remove())
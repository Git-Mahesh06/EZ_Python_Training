class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()

s = Stack()
st = input("Enter the expression: ")
res = 0
for i in st.split():
    if i.isdigit():
        data = int(i)
        s.push(data)
    else:
        op2 = s.pop()
        op1 = s.pop()
        if i == '+':
            res = op1 + op2
        elif i == '-':
            res = op1 - op2
        elif i == '*':
            res = op1 * op2
        elif i == '/':
            res = op1 / op2
        elif i == '%':
            res = op1 % op2
        s.push(res)
print("Result:", s.pop())

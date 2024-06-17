def find_supervisors(arr):
    n = len(arr)
    result = [-1] * n  # Initialize the result array with -1
    stack = []  # Stack to keep track of indices

    # Traverse the list from right to left
    for i in range(n-1, -1, -1):
        # Maintain the elements in decreasing order in the stack
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        
        # If stack is not empty, the top element is the next greater element
        if stack:
            result[i] = arr[stack[-1]]
        
        # Push the current index onto the stack
        stack.append(i)
    
    return result

# Example usage
input_array = [3, 5, 2, 14, 5, 3, 7, 9, 4, 6, 9, 4, 2, 5, 3]
output = find_supervisors(input_array)
print(output)


# Superior code
class Stack:
    def __init__(self):
        self.item = []
    def push(self,data):
        self.item.append(data)
    def pop(self):
        return self.item.pop()
    def size(self):
        return len(self.item)
l=[3, 5, 2, 14, 5, 3, 7, 9, 4, 6, 9, 4, 2, 5, 3]
O=[0]*len(l)
s=Stack()
for i in range(len(l)-1,-1,-1):
    while s.size != 0 and s.top()<l[i]:
        if s.top() <= l[i]:
            s.pop()
        if s.size()==0:
            O[i]=-1
        else:
            O[i]=s.top()
        s.push(l[i])
print(O)
        

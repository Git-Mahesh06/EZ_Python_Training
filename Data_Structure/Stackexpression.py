class Stack:
    def __init__(self):
        self.item = []   
    def push(self,data):
        self.item.append(data)
    def pop(self):
        return self.item.pop()
    # def priority(self,pi):
    #     if pi


# st=input("Enter the string")
# c=[]
# s=Stack()
# for i in st:
#     if i=="(" or i=="{" or i=='[':
#         s.push(i)
#     elif i==')' or i=='}' or i==']':
#         while s.pop()!=')':
#             c.append(s.pop())
#         s.pop()
    
# print(c)

e="[3+7(52/11(3+5)})]"
S=Stack()
ob="[{("
cb="})]"
flag=0
for i in e:
    if i in ob:
        S.push("{")
    if  i in cb:
        x=S.pop()
        if x=="{" and i=="}":
            pass
        elif x=="[" and i=="]":
            pass
        else:
            flag==1
            break
if(flag==0):
    print("valid")
else:
    print("invalid")
            
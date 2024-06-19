l=[int(x) for x in (input("Enter the elements")).split()]
n=len(l)
for j in range(0,n):
    for i in range(0,n-1-j):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print(l)

#find minimum in list
min=l[0]
print("minimum ",min)
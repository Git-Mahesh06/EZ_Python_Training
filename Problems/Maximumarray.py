li=[1,2,3,4,5,6,7,8,9]
li1=[]
for i in range(len(li)-n+1):
    s=li[i:i+3]
    a=sum(s)
    li1.append(a)
m = max(li1)
print(m)
l=li1.index(m)
print("elements are: ",li[l:l+3])


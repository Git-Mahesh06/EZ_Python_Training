def count(li):
    c=0
    for i in range(0,len(li)):
        for j in range(1,len(li)):
            if i==j:
                print(i)
                c+=1
    print(c)

l=[1,2,3,1]
count(l)
#7897001231

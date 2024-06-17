ar=[1,1,0,1,1]

for i in range(len(ar)):
    left=ar[:i]
    print("Left ",left)
    s1=sum(left)
    print(s1)
    right=ar[i:]
    print("Right ",right)
    s2=sum(right)
    print(s2)
    if s1==s2:
        print("Position of element is",i," value is",ar[i])
        break
    
    
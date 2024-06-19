def mergesort(l,left,right):
    if left < right:
        mid=(left+right)//2
        mergesort(l,left,mid)
        mergesort(l,mid+1,right)
        merge(l,left,mid,right)

def merge(l,left,mid,right):
    leftlist=l[left:mid+1]
    rightlist=l[mid+1:right+1]
    i=j=0
    k=left
    while i<len(leftlist) and j<len(rightlist):
        if leftlist[i]<= rightlist[j]:
            l[k]=leftlist[i]
            i+=1
        else:
            l[k]=rightlist[j]
            j+=1
        k+=1
    while i<len(leftlist):
        l[k]=leftlist[i]
        i+=1
        k+=1
    while j<len(rightlist):
        l[k]=rightlist[j]
        j+=1
        k+=1
if __name__ == "__main__":
    L = [int(x) for x in input("Enter the elements ").split()]
    mergesort(L,0,len(L)-1)
    print(L)
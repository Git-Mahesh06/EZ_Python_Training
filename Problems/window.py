l=[2,4,3,5,6,3,4,6,7,9,9,9]
window = max = 0
k = int(input("Enter the no of continious digit: "))

for j in range(0,k):
        window+=l[j]
        # print(window)
l.append(0)
print(l)
for i in range(0,len(l)-k):
    if max<window:
        max=window
        pos=i
    window = window+l[i+k]-l[i]

print("result")
print(max)
for j in range(0,k):
    print(l[pos+j])

def even(n):
    if n%2==0:
        return n
n = int(input().strip())
if n>=2 and n<=6 and even(n):
    print("Not Weird")
elif n and even(n):
    print("Weird")
elif n>20 and even(n):
    print("Not Weird")
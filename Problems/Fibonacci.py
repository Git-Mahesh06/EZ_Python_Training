def fibonacci(n):
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib
n=int(input("enter the number"))
print(fibonacci(n))


# n=int(input("Enter the number"))
# a,b=0,1
# print(a)
# for _ in range(n):
#     a,b=b,a+b
#     print(a)
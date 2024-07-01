w=[4,5,6,3,2,5,4,6,6]
p=[20,10,6,9,18,12,16,30,15]
pw={}
max_profit=30
profit=0
for i in range(len(p)):
    c=p[i]/w[i]
    pw[i]=c
print('Profit/weight ratio ',pw)
for i in pw:
    max=0
    if max < pw[i]:
        max=pw[i]
        j=i
    max_profit-=w[j]
    profit+=p[j]
    pw[i]=0
print(profit)



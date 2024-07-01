def dfs(a,v,s,e):
    if v[e]==False:
        s.append(e)
        v[e]=True:
    else:
        return 
    for i in a[e]:
        dfs(a,v,s,i[1])
    print(s.pop())

v=[]
s=[]
graph={
    1:[]
}

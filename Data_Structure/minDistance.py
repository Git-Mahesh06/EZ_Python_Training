dist = [[1,2,2,3],
        [3,1,4,2],
        [1,5,3,3],
        [1,2,1,1]]

n = len(dist)-1
m = len(dist[0])-1
i = j = 0
sum = dist[i][j]
while i < n or j < m:
    if i == n:
        j+=1
    elif j == m:
        i+=1
    elif dist[i][j+1] < dist[i+1][j]:
        j+=1
    else:
        i+=1
    sum+=dist[i][j]
print(sum)

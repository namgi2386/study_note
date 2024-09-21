n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
    for j in range(3):
        arr[i][j] += min(arr[i-1][(j+1)%3] ,arr[i-1][(j+2)%3])

print(min(*arr[n-1]))
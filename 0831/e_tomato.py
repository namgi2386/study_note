import sys
sys.stdin = open('z4.txt' , 'r')

dr =[-1,0,1,0]
dc =[0,1,0,-1]

def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<m

def g(start_arr):
    new_arr =[]
    for s in range(len(start_arr)):
        r = start_arr[s][0]
        c = start_arr[s][1]
        for d in range(4):
            nr = r + dr[d] 
            nc = c + dc[d]
            if is_valid(nr,nc) and not arr[nr][nc] and not visited[nr][nc] :
                new_arr.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1
                arr[nr][nc] = 1
    return new_arr

m,n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited =[[0]*m for _ in range(n)]

start_arr =[]

for i in range(n):
    for j in range(m):
        if arr[i][j] ==1:
            start_arr.append((i,j))
            visited[i][j] = 1
while start_arr:
    start_arr = g(start_arr)

result = 0
for i in range(n):
    result = max(result , max(visited[i])) 

for i in range(n):
    if 0 in arr[i]:
        result = 0

print(result-1)
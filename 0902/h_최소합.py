import sys
sys.stdin = open('z3.txt' , 'r')

def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def f():
    visited[0][0] = arr[0][0]
    q.append((0,0))
    while q:
        r,c = q.pop(0)
        if (r,c) == (n-1,n-1):
            return visited[n-1][n-1]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr,nc) :
                if visited[r][c] + arr[nr][nc] < visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + arr[nr][nc]
                    q.append((nr,nc))



for tc in range(1,int(input()) +1):
    n = int(input())
    arr =[list(map(int,input().split())) for _ in range(n)]
    q =[]
    result = 0
    for i in range(n):
        result += sum(arr[i])
    visited = [[result]*n for _ in range(n)]
    print(f'#{tc} {f()}')
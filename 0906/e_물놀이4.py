import sys
sys.stdin = open('z2.txt','r')

from collections import deque

dr=[1,0,-1,0]
dc=[0,-1,0,1]

def wata(n,m):
    result = 0
    while q:
        r,c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<= nr<n and 0<=nc<m and  visited[nr][nc]==-1:
                visited[nr][nc] = visited[r][c] +1
                q.append((nr,nc))
                result += visited[nr][nc]
    return result



for tc in range(1, int(input())+1):
    n,m = map(int ,input().split())
    arr = [list(input()) for _ in range(n) ]
    visited = [[-1]*m for _ in range(n) ]
    q=deque()

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                # for d in range(4):
                #     nr = i + dr[d]
                #     nc = j + dc[d]
                #     if 0<= nr<n and 0<=nc<m and arr[nr][nc]=='L':
                visited[i][j] = 0
                q.append((i,j))
    result = wata(n,m)

    print(f'#{tc} {result}')
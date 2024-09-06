import sys
sys.stdin = open('z2.txt','r')

from collections import deque

def is_valid(nr,nc):
    return 0<= nr<n and 0<=nc<m

dr=[1,0,-1,0]
dc=[0,-1,0,1]

def wata():
    while q:
        r,c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr,nc) and arr[nr][nc] == 'L' and  visited[nr][nc] > visited[r][c] +1:
                visited[nr][nc] = visited[r][c] +1
                q.append((nr,nc))





for tc in range(1, int(input())+1):
    n,m = map(int ,input().split())
    arr = [list(input()) for _ in range(n) ]
    visited = [[n*m]*m for _ in range(n) ]
    q=deque()

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                for d in range(4):
                    nr = i + dr[d]
                    nc = j + dc[d]
                    if is_valid(nr,nc) and arr[nr][nc]=='L':
                        visited[i][j] = 0
                        q.append((i,j))
    wata()

    result = 0
    for i in range(n):
        result += sum(visited[i])

    print(f'#{tc} {result}')
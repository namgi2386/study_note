from collections import deque
import sys
sys.stdin = open('z5.txt', 'r')

dr = [-1,1,0,0]
dc = [0,0,1,-1]

def is_valid(n , nr, nc):
    return 0<=nr<n and 0<=nc<n

def miro():

    visited = [[0]*n for _ in range(n)]


    q =deque()
    visited[1][1] = 1
    q.append((1,1))

    while q:
        r,c = q.popleft()

        if maze[r][c] == 3 :
            return 1
        
        for d in range(4):
            nr = r + dr[d]
            nc = c+ dc[d]
            if is_valid(n,nr,nc) and maze[nr][nc] != 1 and not visited[nr][nc] :
                q.append((nr,nc)) 
                visited[nr][nc] = 1
    return 0


T = 10
for tc in range(1,T+1):
    input()
    n = 16
    maze =[ list(map(int,input())) for _ in range(n)]
    result = miro()
    print(f'#{tc} {result}')


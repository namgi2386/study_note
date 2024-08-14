from collections import deque
import sys
sys.stdin = open('z4.txt', 'r')

dr = [1,-1,0,0]
dc = [0,0,1,-1]
def is_valid(n, r,c):
    return 0<=r<n and 0<=c<n


def miro_point(n,arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 3:
                end_point = (i,j)
            if arr[i][j] == 2:
                start_point = (i,j)
    return start_point

def miro(n,s):
    visited =[[0]*n for _ in range(n)]
    q = deque()
    q.append(s)
    visited[s[0]][s[1]] = 0

    while q:
        r,c  = q.popleft()

        if arr[r][c] == 3:
            return visited[r][c]-1

        for d in range(4):
            nr = r+ dr[d]
            nc = c + dc[d]
            if is_valid(n,nr, nc) and not visited[nr][nc] and arr[nr][nc] != 1:
                # nr,nc 방문가능위치
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    return 0



T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr =[ list(map(int,input())) for _ in range(n)]
    s = miro_point(n,arr)
    r = miro(n,s)
    print(f'#{tc} {r}')
    # s= [4,4]   e=[0,1]


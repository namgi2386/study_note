import sys
sys.stdin = open('z1.txt' , 'r')
dr = [-1,0,1,0]
dc = [0,1,0,-1]

def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<m

def butterfly():
    visited = [[0]*m for _ in range(n)]
    counts = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visited[i][j]:
                s= [(i,j)]
                counts += 1
                while s:
                    di,dj = s.pop()
                    for d in range(4):
                        nr = di + dr[d]
                        nc = dj + dc[d]
                        if is_valid(nr,nc) and arr[nr][nc] and not visited[nr][nc]:
                            s.append((nr,nc))
                            visited[nr][nc] = 1
    return counts



T=int(input())
for tc in range(1,T+1):
    n,m,k = map(int,input().split())

    arr = [[0]*m for _ in range(n)]
    for _ in range(k):
        i , j = map(int,input().split())
        arr[i][j] = 1
    # 배추밭 완성

    print(butterfly())


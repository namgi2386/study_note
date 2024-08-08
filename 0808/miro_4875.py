def dfs2(i,j,n):
    visited[i][j] = 1
    if maze[i][j] ==3: return 1
    else:
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj = i+di , j+dj
            if 0<=ni<n and 0<=nj<n and maze[ni][nj] !=1 and visited[ni][nj]==0:
                if dfs2(ni,nj,n):
                    return 1
        return 0

def fstart(n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return  i,j
    return -1,-1


T =int(input())
for tc in range(1,T+1):
    n = int(input())
    maze = [list(map(int,input().split())) for _ in range(n)]

    sti ,stj = fstart(n)

    visited = [[0]*n for _ in range(n)]
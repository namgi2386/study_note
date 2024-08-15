import sys
sys.stdin = open('z3.txt' , 'r')

def is_valid(nr,nc):
    return 0 <= nr < n and 0 <= nc < n and visited[arr[nr][nc]] == 0

def flower(r,c,w,counts,move):
    global max_count
    
    if w==3 and i==r:
        if counts > max_count:
            max_count = counts
        return
    
    if w==2 and i+j == r+c:
        flower(r,c,w+1,counts,0)
        return

    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]
    nr = r + dr[w]
    nc = c + dc[w]

    if is_valid(nr,nc):
        visited[arr[nr][nc]] = 1
        flower(nr,nc,w,counts+1,1)
        visited[arr[nr][nc]] = 0
    if w<2 and move:
        flower(r,c,w+1,counts,0)

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visited = [0 for _ in range(101)]
    max_count = 0
    
    for i in range(n):
        for j in range(n):
            flower(i,j,0,0,0)
    if max_count == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max_count}')

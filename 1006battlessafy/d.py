import sys
sys.stdin = open('z1.txt' , 'r')

from collections import deque



def bfs(my_r,my_c,turret_r , turret_c):
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    q = deque()
    cnt = 0
    result = []
    total_cnt = int(1e9)
    q.append((my_r,my_c,cnt,[]))
    while q:
        r,c,cnt ,load_arr = q.popleft()
        print(r,c,map_data[r][c])

        flag = False
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<nr<=n and 0<nc<=m and map_data[nr][nc]=='X':
                if total_cnt > cnt:
                    total_cnt = cnt
                    result = load_arr[:]
                    flag = True
                    break
        if flag:
            continue

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<nr<=n and 0<nc<=m and map_data[nr][nc] in('G',) and visited[nr][nc] == 0:
                load_arr.append((nr,nc))
                q.append((my_r,my_c ,cnt+1, load_arr))
                load_arr.pop()
    print(result,'re')
    return result


map_data = [list(input().split()) for _ in range(5)]
n = len(map_data)
m = len(map_data[0])
visited = [[0]*(n) for _ in range(m)]
my_r = 4
my_c = 0
turret_r = 0 
turret_c = 5
result = bfs(my_r,my_c,turret_r , turret_c)
print(result,'ens')
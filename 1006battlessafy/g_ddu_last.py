from collections import deque

# 주어진 그리드
map_data = [
    ['G', 'G', 'G', 'A', 'X'],
    ['G', 'G', 'G', 'G', 'G'],
    ['T', 'G', 'G', 'E1', 'G'],
    ['G', 'G', 'G', 'G', 'G'],
    ['G', 'G', 'G', 'G', 'G']
]

def bfs_shortest_path(map_data, sr, sc):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    n = len(map_data)
    m = len(map_data[0])
    q = []
    q.append(( sr, sc, [] ))
    visited = [[0]*m for _ in range(n)]
    visited[sr][sc] = 1
    
    while q:
        r, c,  path = q.pop(0)
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if 0 <= nr < len(map_data) and 0 <= nc < len(map_data[0]) and not visited[nr][nc]:
                if map_data[nr][nc] == "X":
                    return path + [(nr, nc, d)]
                elif map_data[nr][nc] == 'G':
                    visited[nr][nc] = 1
                    q.append((nr, nc, path + [(nr, nc, d)]))
    return None


# 시작점 찾기
sr, sc = -1, -1
for i in range(len(map_data)):
    for j in range(len(map_data[0])):
        if map_data[i][j] == 'A':
            sr, sc = i, j
            break
    if sr != -1:
        break


# BFS로 최단 경로 찾기
path_to_x = bfs_shortest_path(map_data, sr, sc)
go_r = path_to_x[0][0]
go_c = path_to_x[0][1]
point = path_to_x[0][2]
if map_data[go_r][go_c] == 'X': # 도착일때 공격
    attack_li = [  'U F' ,'D F', 'L F' , 'R F' ]
    output = attack_li[point]
else: 
    run_li = [ 'U A' , 'D A' , 'L A', 'R A'   ]
    output = run_li[point]
print(output)

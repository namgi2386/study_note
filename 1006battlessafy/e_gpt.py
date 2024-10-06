from collections import deque

def bfs_shortest_path(grid, start_x, start_y, end_char):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    queue = deque([(start_x, start_y, [])])
    visited = set()
    visited.add((start_x, start_y))
    
    while queue:
        x, y, path = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                if grid[nx][ny] == end_char:
                    return path + [(nx, ny)]
                elif grid[nx][ny] == 'G':
                    visited.add((nx, ny))
                    queue.append((nx, ny, path + [(nx, ny)]))
    
    return None

# 주어진 그리드
grid = [
    ['G', 'G', 'T', 'G', 'X'],
    ['G', 'G', 'T', 'G', 'G'],
    ['G', 'G', 'G', 'E1', 'G'],
    ['A', 'T', 'G', 'T', 'G'],
    ['G', 'G', 'G', 'G', 'G']
]

# 시작점 찾기
start_x, start_y = -1, -1
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'A':
            start_x, start_y = i, j
            break
    if start_x != -1:
        break

if start_x == -1:
    print("시작점 A를 찾을 수 없습니다.")
else:
    # BFS로 최단 경로 찾기
    path_to_x = bfs_shortest_path(grid, start_x, start_y, 'X')
    
    if path_to_x:
        print("이동 경로의 좌표들:")
        for coord in path_to_x:
            print(coord)
    else:
        print("목표지점 X에 도달할 수 없습니다.")

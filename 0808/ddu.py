T = int(input())
 
for tc in range(1, T+1):
    n = int(input()) # n*n행렬의 n
    maze = [list(input()) for _ in range(n)] # maze의 값은 str!!
    visited = [[0] * n for _ in range(n)] # 지나온 곳 기록하기
    r,c = 0,0 # 출발지점
 
    for i in range(n): # 미로에서 2 찾기
        for j in range(n):
            if maze[i][j] == '2': # maze값이 str이니까 int로 바꿔야대!!
                r,c = i,j
 
    visited[r][c] = 1 # 출발지점 방문표시
    stack = [(r,c)]
    found = False
 
    while stack: # 스택이 비어있으면 탈출
        r,c = stack.pop()
        if maze[r][c] == '3': # 현재위치가 도착지점이면
            found = True
            break
        else: # 도착지점이 아니면
            for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                nr,nc = r+di,c+dj
                if 0<=nr<n and 0<=nc<n and maze[nr][nc] != '1' and visited[nr][nc] == 0:
                    visited[nr][nc] = 1 # 이동한 지점 방문표시
                    stack.append((nr,nc)) # 스택에 저장
 
    if found:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
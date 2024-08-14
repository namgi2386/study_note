from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1] # 문제에따라 변경가능

N = 7
maze = [[0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 1, 0],
        [1, 0, 1, 9, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0],
        [0, 0, 1, 0, 0, 0, 0]]

def where_i_am(r,c,n):
    temp = maze[r][c]
    maze[r][c] = '*'
    for i in range(n):
        print(maze[i])
    maze[r][c] =temp
    print()
    return


def is_valid(r,c):
    return 0<=r<N and 0<=c<N

def bfs(sr,sc):
    visited = [[0]*N for _ in range(N) ]
    q = deque()

    q.append((sr,sc)) # 상황에 따라 변수추가 가능
    visited[sr][sc] = 1 # 시작점 추가하고 시작하기

    # 모든 위치탐색
    while q:
        r,c = q.popleft()

        where_i_am(r,c,N)

        if maze[r][c] == 9:
            print(f'탈출! :  {r},{c} , 거리 : {visited[r][c]}')
            return True

        for d in range(4): #현재지점기준 4개방향 체크
            nr = r + dr[d]
            nc = c + dc[d]

            # nr,nc가 범위 안인지 체크
            # 방문한 적 없어야함
            # 벽이 아니어야 함
            if is_valid(nr,nc) and not visited[nr][nc] and maze[nr][nc] != 1:
                # nr,nc 방문가능위치
                q.append((nr,nc)) # 가야할 위치로 추가해놓기
                visited[nr][nc] = visited[r][c] + 1 # 거리계산

    print('탈출실패')
    return False

bfs(0,0)
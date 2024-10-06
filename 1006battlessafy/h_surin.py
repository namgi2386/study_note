import sys
sys.stdin = open('z3.txt')
# bfs
from collections import deque
    # 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    ground = [list(map(str,input())) for _ in range(N)]
    visited = [[9999]*N for _ in range(N)]
    min_road = 99999
    # Queue = y 를 넣고 0 으로 만든다음
    # 주변을 다 1로 만들어
    # X 부터 Y 까지 가는 거리를 다 더해
    # T를 만난다면 +1
    # 단 T를 만난 횟수가 M 을 넘으면 그 로드는 버리기
    # 그렇게 나온 최솟값을 뽑아내기

    queue = deque()
    # 도착 지점 찾기
    for i in range(N):
        for j in range(N):
            # 출발
            if ground[i][j] == 'X':
                queue.append((i,j))
                visited[i][j] = 1

            # elif ground[i][j] == 'T':
            #     visited[i][j] = 2

            # # 도착
            # elif ground[i][j] == 'Y':
            #     visited[i][j] = 0
    cnt = 0
    while queue:
        destination_x, destination_y = queue.popleft()
        for d in range(4):
            nx = destination_x + dx[d]
            ny = destination_y + dy[d]

            # 범위를 벗어나면
            if 0 > nx or nx >= N or 0 > ny or ny >= N:
                continue

            # 방문한 적이 있으면
            if visited[nx][ny] != 9999:
                continue

            # 나무를 베는 횟수 세기
            # 그렇지 않으면
            if ground[nx][ny] == "T":
                cnt += 1

            # 나무를 벤 횟수가 M 을 넘기면 그 경로는 무시
            if cnt > M:
                continue

            # 도착지에 도착하면
            if visited[nx][ny] == 0:
                if min_road > visited[nx][ny]:
                    min_road = visited[nx][ny]

            # 다음 탐색을 위한 좌표
            visited[nx][ny] = visited[destination_x][destination_y]+ 1
            queue.append((nx,ny))

    print(f"#{tc} {min_road}")
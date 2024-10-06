from collections import deque
import sys

sys.stdin = open('z3.txt' , 'r')
# 상, 우, 하, 좌 방향 정의
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# BFS 탐색 함수
def bfs(N, K, field, start, end):
    dq = deque([(start[0], start[1], 0, 0, 0)])  # 시작 (r, c), 방향(상:0), 나무 벤 횟수, 조작 횟수
    visited = set()  # 방문 기록 (r, c, 방향, 벤 나무의 수)
    visited.add((start[0], start[1], 0, 0))


    while dq:
        r, c, d, cut, moves = dq.popleft()



        # 목적지에 도착한 경우
        if (r, c) == end:
            return moves


        # 1. 전진
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < N:
            if field[nr][nc] in ('G','Y') and (nr, nc, d, cut) not in visited:
                visited.add((nr, nc, d, cut))
                dq.append((nr, nc, d, cut, moves + 1))
            elif field[nr][nc] == 'T' and cut < K and (nr, nc, d, cut + 1) not in visited:
                # 나무를 벨 수 있는 경우
                visited.add((nr, nc, d, cut + 1))
                dq.append((nr, nc, d, cut + 1, moves + 1))

        # 2. 왼쪽 회전
        nd = (d + 3) % 4
        if (r, c, nd, cut) not in visited:
            visited.add((r, c, nd, cut))
            dq.append((r, c, nd, cut, moves + 1))

        # 3. 오른쪽 회전
        nd = (d + 1) % 4
        if (r, c, nd, cut) not in visited:
            visited.add((r, c, nd, cut))
            dq.append((r, c, nd, cut, moves + 1))

    return  (tc,end)


# 문제 해결 함수
def drive(N, K, field):
    start = end = None
    # RC카의 시작점과 목적지 찾기
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                start = (i, j)
            elif field[i][j] == 'Y':
                end = (i, j)
    # BFS 탐색 시작
    return bfs(N, K, field, start, end)



T = int(input()) 

for tc in range(1, T + 1):
    # N: 필드 크기, K: 나무를 벨 수 있는 횟수
    N, K = map(int, input().split())
    field = [input() for _ in range(N)]

    # drive 함수 호출
    result = drive(N, K, field)

    # 결과 출력
    print(f'#{tc} {result}')

import sys
sys.stdin = open('z3.txt' , 'r')

def is_valid(nr,nc):
    return 0 <= nr < n and 0 <= nc < n and visited[arr[nr][nc]] == 0

def recur(cur, r, c, cnt, move): # recur(0, i, j, 0, 0)
    global max_cnt
    if cur == 3 and i == r:             # 사각형 완성했을 때
        if cnt > max_cnt:
            max_cnt = cnt
        return
    if cur == 2 and i + j == r + c:     # 두 변을 그린 후부터는 변의 길이에 맞춰 잇는다.
        recur(cur + 1, r, c, cnt, 0)    # 마지막 세번째 꺾고 시작점으로 잇는다.
        return
    # 가던 방향으로 움직인다.
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]
    nr = r + dr[cur]
    nc = c + dc[cur]
    if is_valid(nr,nc):
        visited[arr[nr][nc]] = 1        # 방문 표시
        recur(cur, nr, nc, cnt + 1, 1) # 1점추가 , move=1 체크후 재귀
        visited[arr[nr][nc]] = 0        # 재귀를 빠져 나오면 방문 표시 제거

    # 방향 전환 - 2번까지 임의로 꺾고 3번부터는 사각형을 그리니 임의로 꺾지 않는다.
    if cur < 2 and move:    # 한 번이라도 움직였을 때 꺾는다.
        recur(cur + 1, r, c, cnt, 0)


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(101)]       # 중복 확인하기 위함
    max_cnt = 0                             # 출력할 결과

    for i in range(n):          # 모든 점에서 start
        for j in range(n):
            recur(0, i, j, 0, 0) # recur(cur(방향0123), r, c, cnt(방문횟수,결과값), move)

    if max_cnt == 0:            # 사각형을 그릴 수 없으면 -1 출력
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max_cnt}')
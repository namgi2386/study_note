T = int(input())

#    상 하 좌 우
dr = [-1,1,0,0] # 행 번호 변화량
dc = [0,0,-1,1] # 열 번호 변화량

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = -9999 # (문제에서 음수가 범위에 있으므로 가능한 작은값도 음수)
    # 모든 위치에서 최대값 구해보자
    # 현재위치 (r,c)
    for r in range(N):
        for c in range(N):
            food = arr[r][c]
            for d in range(4): # 4방향 탐색
                nr = r + dr[d]
                nc = r + dc[d]
                if 0 <= nr < N and 0 <= nc < N: # 인덱스 유효성 검사
                    food += arr[nr][nc]
            if answer < food:
                answer = food


    print(f'#[tc} {answer}')




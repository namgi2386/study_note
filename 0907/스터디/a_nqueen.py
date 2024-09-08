T = int(input())

def find_q(x,y): # 위쪽 대각선에 퀸이 있는지 확인
    for i in range(2):
        for j in range(1,n):
            nx, ny = x + j*dx[i], y + j*dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if case[nx][ny] == 1:
                    return False
    return True

def permu(k): # k = 가로열
    # print(k)
    if k == n: # 모든 줄에 퀸을 놓았다면 정답 +1
        ans[0] += 1
        # print(visit)
        return
    for m in range(n): # 세로열 확인
        if visit[m] == 0: # 세로열m에 퀸을 놓은 적이 없고
            if find_q(k,m) == True: # 윗쪽 퀸에 영향을 받지 않는다면
                visit[m] = 1 # m번 세로열은 체크(동일한 세로열에 놓는 걸 방지)
                case[k][m] = 1 # 체스판에 퀸 올리기 (k,m)dp
                permu(k+1) # 다음 가로줄로 이동
                visit[m] = 0 # 돌아오면 초기화
                case[k][m] = 0 # 돌아오면 초기화
            
dx = [-1,-1]
dy = [-1,1]
for t in range(1,T+1):
    n = int(input())
    case = [[0]*n for _ in range(n)]
    visit = [0]*n
    ans = [0]
    permu(0)
    print(f'#{t} {ans[0]}')
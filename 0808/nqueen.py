
# 재귀함수를 사용한다
# 종료조건은 행하나당 퀸하나씩 놓을건데, 0행부터 놓기시작해서 n까지 도착하면 끝
# 혹은 남은 퀸의 갯수가 없을때 종료

# r : 내가 r번째 행에 퀸을 놓을지 말지 선택 중
# n : 남은 퀸의 갯수
def place_queen(r,n):
    global count
    # 0. 가지치기(선택)
    # 1. 종료조건
    if n == 0 and r == N :
        # 퀸을 n개 놓는 경우의 수 발견!
        count += 1
        return
    # 2. 재귀호출
        # 내가 r번째 행에 퀸을 놓았다면 다음행 ㄱㄱ
        # 놓지 않았다면 다음진행불가능
    # r번째 행에 c번 열에 퀸을 놓을지 선택
    for c in range(N):
        can_place = True
        # 놓지 못하는 자리라면  can_place = False 바꿀거임

        # 윗칸 검사
        for i in range(r):
            if board[i][c] == 1:
                can_place = False
                break
        # 좌상단 + 우상단 검사
        for i in range(1, r+1):
            if r-i >=0 and c-i >=0 and board[r-i][c-i] ==1:
                can_place = False
                break
            if r-i >=0 and c+i <n and board[r-i][c+i] ==1:
                can_place = False
                break

        # 검사가 끝난이후 다음행으로 갈수있다면 재귀호출
        if can_place:
            # r+1번째 행으로 퀸을 놓으러 가자
            board[r][c] = 1 # 현재 위치에 퀸 놓았다고 표시
            place_queen(r+1,n-1) # 다음 행으로 퀸 놓으러 가기

            #(r,c)에서 퀸을 놓고 진행했던 상황 검사가 모두 끝나면
            # 다시 원상 복귀 ( importanta! )
            board[r][c] = 0





T = int(input())
for tc in range(1,T+1):
    N = int(input())
    count = 0

    # 체스판만들기
    board = [[0]*N for _ in range(N)]
    # board[r][c] 값이 0이면 빈칸 1이면 퀸있음상태
    place_queen(0, N)

    print(f"#{tc} {count}")
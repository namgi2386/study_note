


# r : 내가 r번째 행에 퀸을 놓을지 말지 선택하고 있다.
# n : 남은 퀸의 개수
def place_queen(r, n):
    global count
    if n == 0 and r == N:
        count += 1
        return
    for c in range(N):
        can_place = True
        for i in range(r):
            # (i,c) 위치에 퀸이 있나 검사
            if board[i][c] == 1:
                can_place = False
                break

        for i in range(1, r + 1):
            # 좌상 대각선 검사
            if r - i >= 0 and c - i >= 0 and board[r - i][c - i] == 1:
                # 좌상 대각선으로 가다가 퀸 발견 => 불가능
                can_place = False
                break

            # 우상 대각선 검사
            if r - i >= 0 and c + i < N and board[r - i][c + i] == 1:
                # 우상 대각선으로 가다가 퀸 발견 => 불가능
                can_place = False
                break

        # 위쪽 검사 끝내고 다음 행으로 갈수 있으면 => 재귀 호출
        if can_place:
            # r + 1 번째 행으로 퀸을 놓으러 가자
            board[r][c] = 1  # 현재 위치에 퀸 놓았다고 표시
            place_queen(r + 1, n - 1)  # 다음 행으로 퀸 놓으러 가자/;l

            # (r,c)에서 퀸을 놓고 진행했던 상황 검사가 모두 끝나면
            # 다시 원상 복귀(아주 중요!!!)
            board[r][c] = 0

        # 갈수 없으면 그냥 종료


for tc in range(1, T + 1):
    N = int(input())
    count = 0
    board = [[0] * N for _ in range(N)]
    place_queen(0, N)

    print(f"#{tc} {count}")

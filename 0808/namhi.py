T = int(input())

def place_queen(r, n):
    global count
    # if count == 1:
    #     return
    if n == 0 and r == N:
        count += 1
        return
    for c in range(N):
        can_place = True
        for i in range(r):
            if board[i][c] == 1:
                can_place = False
                break
        for i in range(1, r + 1):
            if r - i >= 0 and c - i >= 0 and board[r-i][c-i] == 1:
                can_place = False
                break
            if r-i >=0 and c+i < N and board[r-i][c+i] == 1:
                can_place = False
                break
        if can_place:
            board[r][c] = 1
            place_queen(r+1, n-1)  # 1 2 3층  (4층 리턴)

            board[r][c] = 0

for tc in range(1, T+1):
    N = int(input())
    count = 0
    board = [[0]*N for _ in range(N)]
    place_queen(0, N)
    print(f"#{tc} {count}")


#place_queen(0, 4)

def place_queen(r,n):

    if n == 0 and r == MAX_N :   ### 
        count += 1
        return
    
    for c in range(MAX_N):

        can_place = True

        for i in range(r):
            if board[i][c] == 1:
                can_place = False
                break
        for i in range(1, r+1):
            if r-i >=0 and c-i >=0 and board[r-i][c-i] ==1:
                can_place = False
                break
            if r-i >=0 and c+i <MAX_N and board[r-i][c+i] ==1:
                can_place = False
                break

        if can_place:
            board[r][c] = 1 
            place_queen(r+1,n-1)
            
            board[r][c] = 0





T = int(input())
for tc in range(1,T+1):
    MAX_N = int(input())
    count = 0

    # 체스판만들기
    board = [[0]*MAX_N for _ in range(MAX_N)]
    # board[r][c] 값이 0이면 빈칸 1이면 퀸있음상태
    place_queen(0, MAX_N)

    print(f"#{tc} {count}")
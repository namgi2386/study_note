import sys
sys.stdin = open('z2.txt' , 'r')

def mongshell(n):

    matrix = [[0]*(n) for _ in range(n)] # 게임준비
    # /  0  1  2  3 
    # 0 [ ][ ][ ][ ]
    # 1 [ ][W][B][ ]
    # 2 [ ][B][W][ ]
    # 3 [ ][ ][ ][ ]

    # matrix[n//2][n//2] == matrix[2][2]
    matrix[n//2][n//2], matrix[n//2 -1][n//2 -1] = 'W' , 'W'
    matrix[n//2 -1][n//2] , matrix[n//2][n//2 -1] = 'B' , 'B'
    return matrix

def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n

def osello(matrix):

    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,1,1,1,0,-1,-1,-1]

    for i in range(m):  # 게임시작 돌을 m번 놓을 예정
        r = arr[i][0]-1 # 행
        c = arr[i][1]-1 # 열

        if arr[i][2] == 1: # 흑돌
            matrix[r][c] = 'B'
            
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]
                if is_valid(nr,nc) and matrix[nr][nc] == 'W': # 옆자리가 W일때
                    h=1
                    while is_valid(nr+dr[d]*h,nc+dc[d]*h) and matrix[nr+dr[d]*h][nc+dc[d]*h] == 'W': # 어디까지 w인지 체크
                        h +=1
                    if is_valid(nr+dr[d]*h,nc+dc[d]*h) and matrix[nr+dr[d]*h][nc+dc[d]*h] == 'B': # wwww이후 B 등장시
                        for e in range(h):
                            matrix[nr+dr[d]*e][nc+dc[d]*e] = 'B' # w 전부 B로 만들어주기

        else :             # 백돌
            matrix[r][c] = 'W'

            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]
                if is_valid(nr,nc) and matrix[nr][nc] == 'B': 
                    h=1
                    while is_valid(nr+dr[d]*h,nc+dc[d]*h) and matrix[nr+dr[d]*h][nc+dc[d]*h] == 'B':
                        h +=1
                    if is_valid(nr+dr[d]*h,nc+dc[d]*h) and matrix[nr+dr[d]*h][nc+dc[d]*h] == 'W':
                        for e in range(h):
                            matrix[nr+dr[d]*e][nc+dc[d]*e] = 'W' 
    return matrix

def checking(matrix):
    w_count = 0
    b_count = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'B':
                b_count += 1
            elif matrix[i][j] == 'W':
                w_count += 1
    return (b_count , w_count)





T = int(input())
for tc in range(1,T+1):
    n,m = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(m)]

    board_ready = mongshell(n)
    matrix = osello(board_ready)
    result = checking(matrix)
    print(f'#{tc} {result[0]} {result[1]}')

    

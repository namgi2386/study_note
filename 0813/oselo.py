import sys
sys.stdin = open('z1.txt' , 'r' )

T = int(input())

def setting_mongshell(n,arr):
    matrix = [[0]*(n+1) for _ in range(n+1)] # 게임준비
    # /  0  1  2  3  4
    # 0 [/][/][/][/][/]
    # 1 [/][ ][ ][ ][ ]
    # 2 [/][ ][W][B][ ]
    # 3 [/][ ][B][W][ ]
    # 4 [/][ ][ ][ ][ ]

    # matrix[n//2][n//2] == matrix[2][2]
    matrix[n//2][n//2], matrix[n//2 +1][n//2 +1] = 'W' , 'W'
    matrix[n//2 +1][n//2] , matrix[n//2][n//2 +1] = 'B' , 'B'
    return matrix

def check(n,m,r,c,h):
    return 1

def run_mongshell(n,m,arr,matrix):
    for i in range(m):  # 게임시작
        r = arr[i][0] # 행
        c = arr[i][1] # 열

        
        
        matrix[r][c]



        if arr[i][2] == 1: # 흑돌
            matrix[r][c] = 'B'
            pass
        else :             # 백돌
            matrix[r][c] = 'W'
            pass


for tc in range(1,T+1):
    n,m = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(m)]
    matrix = setting_mongshell(n,arr)
    run_mongshell(n,m,arr,matrix)
    
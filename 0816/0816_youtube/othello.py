import sys
sys.stdin = open('z2.txt' , 'r')

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n

def fight(matrix):
    ma1 = matrix[0]
    ma2 = matrix[1]
    ma3 = matrix[2]
    ma4 = matrix[3]
    for i in range(m):
        r = arr[i][0] -1
        c = arr[i][1] -1
        if arr[i][2] == 1: #흑돌
            matrix[r][c] = 'B'
            for d in range(8):
                h = 1
                side_r = r +dr[d]*h
                side_c = c +dc[d]*h
                while is_valid(r +dr[d]*h ,c +dc[d]*h ) and matrix[r +dr[d]*h][c +dc[d]*h] == 'W':
                    h += 1
                if is_valid(r +dr[d]*h , c +dc[d]*h) and matrix[r +dr[d]*h][c +dc[d]*h] == 'B':
                    for e in range(1,h):
                        matrix[r +dr[d]*e][c +dc[d]*e] = 'B'
        else: # 백돌
            matrix[r][c] = 'W'

            for d in range(8):
                h = 1
                while is_valid(r + dr[d] * h, c + dc[d] * h) and matrix[r + dr[d] * h][c + dc[d] * h] == 'B':
                    h += 1
                if is_valid(r + dr[d] * h, c + dc[d] * h) and matrix[r + dr[d] * h][c + dc[d] * h] == 'W':
                    for e in range(1, h):
                        matrix[r + dr[d] * e][c + dc[d] * e] = 'W'


for tc in range(1,int(input())+1 ):
    n,m = map(int,input().split())

    matrix = [[0]*n for _ in range(n)]
    arr =[list(map(int,input().split())) for _ in range(m)]

    matrix[n//2][n//2] = 'W'
    matrix[n//2-1][n//2-1] = 'W'
    matrix[n//2][n//2-1] = 'B'
    matrix[n//2-1][n//2] = 'B'
    #print(matrix)
    fight(matrix)
    count_b = 0
    count_w = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'B':
                count_b += 1
            elif matrix[i][j] == 'W':
                count_w += 1
    #print(f'{tc} {matrix}')
    print(f'#{tc} {count_b} {count_w}')


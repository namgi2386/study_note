import sys
sys.stdin = open('input (2).txt' , 'r')

T = int(input())

for tc in range(1,T+1):
    n = int(input())

    snail = [[0] * n for _ in range(n)]

    #    0   1   2   3
    #    우  하  좌  상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    d = 0
    r, c = 0, 0

    for i in range(1, n*n+1):
        snail[r][c] = i

        if 0 <= r + dr[d] < n and 0 <= c + dc[d] < n and snail[r + dr[d]][c + dc[d]] == 0 :
            r += dr[d]
            c += dc[d]
        else:
            d = (d+1) % 4
            r += dr[d]
            c += dc[d]

    print(f'#{tc} ')
    for i in snail:
        print(*i)
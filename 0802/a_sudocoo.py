import sys
sys.stdin = open('sudo.txt','r')

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    result = 1

    for i in range(9):
        row_sum =0
        col_sum = 0
        for j in range(9):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        if row_sum != 45 or col_sum != 45 :
            result = 0
    
    d_p = [0,3,6]

    for i in range(3):
        for j in range(3):
            square_sum = 0
            for k in range(3):
                for l in range(3):
                    square_sum += arr[d_p[i]+k][d_p[j]+l] 
            if square_sum != 45:
                result = 0
    
    print(f'#{tc} {result}')

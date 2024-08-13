import sys
sys.stdin = open('z3.txt' , 'r')

T = int(input())

#    12시  1시 3시 ... 총 8개의방향 (시계방향)
dr = [-1, -1, 0, 1, 1,  1,  0, -1]
dc = [0,   1, 1, 1, 0, -1, -1, -1]

def omo():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                for d in range(8):
                    if 0<=i+dr[d]*4<n and 0<=j+dc[d]*4<n:
                        for k in range(1, 5):
                            if arr[i+dr[d]*k][j+dc[d]*k] != 'o':
                                break
                        else :
                            return 'YES'
    return 'NO'

for tc in range(1,T+1):
    n= int(input())
    arr = [list(input()) for _ in range(n)]

    result = omo()
    print(f'#{tc} {result}')
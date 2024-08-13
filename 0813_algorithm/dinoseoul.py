import sys
sys.stdin = open('z5.txt' , 'r')

T = int(input())
dr = [0,1]
dc = [1,0]

for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                for h in range(2):
                    k=0
                    while 0<=i+dr[h]*k < n and 0<=j+dc[h]*k <m and arr[i+dr[h]*k][j+dc[h]*k] == 1:
                        k+= 1
                    if k > result:
                        result = k
    print(f'#{tc} {result}')
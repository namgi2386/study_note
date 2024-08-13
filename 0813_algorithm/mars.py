import sys
sys.stdin = open('z4.txt' , 'r')

T = int(input())

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

def mase():
    result = 0
    for i in range(n):
        for j in range(m):
            counts = 0
            for d in range(8):
                if 0<= i+dr[d]<n and 0<= j+dc[d]<m:
                    if arr[i][j] > arr[i+dr[d]][j+dc[d]]:
                        counts += 1
            if counts >= 4:
                result += 1
    return result

for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    result = mase()
    print(f'#{tc} {result}')
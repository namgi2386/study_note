import sys
sys.stdin = open('z2.txt' , 'r')

T = int(input())

ar = [-1,0,1,0] # 북 > 동남서
ac = [0,1,0,-1]
br = [-1,-1,1,1] # 11시 > 1시
bc = [-1,1,-1,1]

d = 0

def fly(arr):
    result = 0
    for i in range(n):
        for j in range(n):
            counts = arr[i][j]
            counts2 = arr[i][j]
            for h in range(1,m):
                for e in range(4):
                    if 0<=i+ar[e]*h<n and 0<=j+ac[e]*h<n:
                        counts += arr[i+ar[e]*h][j+ac[e]*h]
                    if 0<=i+br[e]*h<n and 0<=j+bc[e]*h<n:
                        counts2 += arr[i+br[e]*h][j+bc[e]*h]
            if counts > result :
                result = counts
            if counts2 > result :
                result = counts2
    return result 


for tc in range(1,T+1):
    n,m = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]

    result = fly(matrix)
    print(f'#{tc} {result}')
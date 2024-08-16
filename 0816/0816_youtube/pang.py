import sys
sys.stdin = open('z1.txt' , 'r')

def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<m

dr = [-1,0,1,0]
dc = [0,1,0,-1]

for tc in range(1,int(input())+1 ):
    n,m = map(int,input().split())
    arr =[list(map(int,input().split())) for _ in range(n)]

    max_counts = 0
    for i in range(n):
        for j in range(m):
            counts = arr[i][j]


            for d in range(4):
                for h in range(1,arr[i][j]+1):
                    nr = i + dr[d]*h
                    nc = j + dc[d]*h
                    if is_valid(nr,nc):
                        counts += arr[nr][nc]
                    else:
                        break
            max_counts = max(max_counts , counts)
    print(f'#{tc} {max_counts}')

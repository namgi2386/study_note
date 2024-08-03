# import sys
# sys.stdin = open('input_bubble.txt','r')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    d = 0

    r , c = 0,0
    for num in range(1,n*n+1):
        arr[r][c] = num

        if 0 <= r + dr[d] < n and 0<= c + dc[d] < n and arr[r + dr[d]][c + dc[d]]==0 :
            r += dr[d]
            c += dc[d]
        else :
            d = (d+1)%4
            r += dr[d]
            c += dc[d]
    
    print(f'#{tc}')
    for i in range(n):
        print(*arr[i])



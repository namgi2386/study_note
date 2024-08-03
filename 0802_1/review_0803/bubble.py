import sys
sys.stdin = open('input_bubble.txt','r')

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_bubbke_pop = 0

    for i in range(n):
        for j in range(m):
            position_sum = arr[i][j]

            for h in range(1, arr[i][j]+1):
                if 0<= i+h <=n-1: # 아랫줄 아니면
                    position_sum += arr[i+h][j]

                if 0<= i-h <= n-1 : # 윗줄 아니면
                    position_sum += arr[i-h][j]

                if 0<= j+h <=m-1:
                    position_sum += arr[i][j+h]
                    
                if 0<= j-h <=m-1 :
                    position_sum += arr[i][j-h]
                
            if position_sum > max_bubbke_pop:
                max_bubbke_pop = position_sum
    
    print(f'#{tc} {max_bubbke_pop}')

import sys
sys.stdin = open('input_bubble.txt','r')

T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_bubble_pop = 0

    for i in range(N):
        for j in range(M):
            position_sum = arr[i][j]
            
            for h in range(1, arr[i][j]+1):
                if  0 <= i+h <= N-1 :
                    position_sum += arr[i+h][j]

                if  0 <= i-h <= N-1 :
                    position_sum += arr[i-h][j]

                if  0 <= j+h <= M-1 :
                    position_sum += arr[i][j+h]

                if  0 <= j-h <= M-1 :
                    position_sum += arr[i][j-h]

            if max_bubble_pop < position_sum :
                max_bubble_pop = position_sum
    
    print(f'#{tc} {max_bubble_pop}')
            
             
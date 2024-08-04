import sys
sys.stdin = open('input1.txt','r')

T = int(input())

for tc in range(1,T+1):
    n , m , power = map(int, input().split() )
    arr = [list(map(int,input().split())) for _ in range(n)]

    max_num = arr[0][0]
    for i in range(n):
        for j in range(m):
            position_sum = arr[i][j]
            for h in range(1,power):
                if i+h < n and j+h < m : 
                    position_sum += arr[i+h][j+h]
                if i-h >= 0 and j-h >= 0 :
                    position_sum += arr[i-h][j-h]
                if i+h < n and j-h >= 0 :
                    position_sum += arr[i+h][j-h]
                if i-h >= 0 and j+h < m :
                    position_sum += arr[i-h][j+h]
            if position_sum > max_num:
                max_num = position_sum

    print(f'#{tc} {max_num}')

# 2 1 1 2 2 
# 2 2 10 2 2 
# 2 2 1 1 2 
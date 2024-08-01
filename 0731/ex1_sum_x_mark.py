import sys
sys.stdin = open('in.txt','r')                               ############
                                                             ##        ##
T = int(input())                                             ##        ##
for tc in range(1,T+1):                                      ##        ##
    n = int(input())                                         ##        ##
    arr = [list(map(int,input().split())) for _ in range(n)] ############

    dia_sum =0
    for i in range(n):
        for j in range(n):
            if i == j :
                dia_sum +=arr[i][j]
            elif i + j == n-1 :
                dia_sum += arr[i][j]

    print(f'sum = {dia_sum}')
    # dia_sum -= arr[n//2][n//2]

    # >>> 347 , 531 , 90
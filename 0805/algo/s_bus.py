import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    p = int(input())
    c_arr =[ int(input()) for _ in range(p)]
    zero_arr = [0]*p

    for i in range(n):
        for j in range(arr[i][0] , arr[i][1] +1):
            for k in range(p):
                if j == c_arr[k]:
                    zero_arr[k] +=1

    print(f'#{tc}', end=" ")
    print(*zero_arr)

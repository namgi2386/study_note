import sys
sys.stdin = open('in.txt','r')

def is_valid(i,j):
    return 0<= i < n and 0 <= j < n

di = [-1, 1, 0, 0]
dj = [0,0,-1,1]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    diff_sum = 0
    for i in range(n):
        for j in range(n):
            now_diff_sum = 0

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if is_valid(ni, nj):
                    diff = arr[i][j] - arr[ni][nj]

                    if diff < 0:
                        diff = -diff

                    now_diff_sum += diff

            diff_sum += now_diff_sum
    print(diff_sum)
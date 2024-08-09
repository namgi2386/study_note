T = int(input())

def minimum_sum(idx, arr, n , mini):
    global min_num
    # 종료조건
    if idx == n:
        if min_num > mini:
            min_num = mini

    # 재귀
    my_sum = 0
    for i in range(n):
        arr[idx][i]


for tc in range(1,T+1):
    N = int(input())
    arr = [ list(map(int,input().split())) for _ in range(N) ]
    min_num = 1000000000000
    minimum_sum(0, arr, N , min_num)
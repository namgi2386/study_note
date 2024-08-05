import sys
sys.stdin = open('algo2_sample_in.txt','r')

T = int(input())
for tc in range(1,T +1):
    n = int(input())
    path = list(map(int,input().split()))

    max_lenght = 0 # 작은값

    min_slope = float('inf') # 매우 큰 값

    l = 1  #오르막의 길이
    start = path[0]

    for i in range(1,n):
        if path[i] >= path[i-1]:
            l += 1
        else:
            if l >= 2:
                slope = (path[i-1] - start) /l

                if slope < min_slope:
                    min_slope = slope
                    max_lenght = l
                elif slope == min_slope:
                    if l > max_lenght:
                        max_lenght = l
            l = 1
            start = path[i]
    if l >= 2:
        slope = (path[-1] - start) / l

        if slope < min_slope:
            min_slope = slope
            max_lenght = l
        elif slope == min_slope:
            if l > max_lenght:
                max_lenght = l
    print(f'#{tc} {max_lenght}')


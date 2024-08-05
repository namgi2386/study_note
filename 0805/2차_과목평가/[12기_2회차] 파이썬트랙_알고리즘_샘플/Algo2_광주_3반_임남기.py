T = int(input())
for tc in range(1,T +1):
    n = int(input())
    arr = list(map(int,input().split()))
    mountain_point = []                     # 경사도 기록하기 위한 리스트
    mountain_lenth = []                     # 경사도가 기록될 때의 경로의 길이를 기록하는 리스트

    start = 0
    for idx in range(n-1):
        if arr[idx] > arr[idx+1]:           # 1. 높이가 낮아지는 순간, 그때의 index , 그리고 시작점을 이용하여 경사도 기록
            path_length = idx - start +1            # 길이
            mountain_lenth.append(path_length)      # 길이 기록
            path_high = arr[idx]                    # 최대높이
            path_low = arr[start]                   # 시작높이

            point = ( path_high - path_low ) / path_length  # 경사도 계산
            mountain_point.append(point)                    # 경사도 기록
            start = idx +1                                                  # 시작지점 갱신

        if idx == n-2 and arr[n-2] < arr[n-1]:      # 마지막 지점에서 높이가 낮아지지 않을때,  경사도를 따로 기록
            path_length = idx - start + 2
            mountain_lenth.append(path_length)
            path_high = arr[idx+1]
            path_low = arr[start]

            point = (path_high - path_low) / path_length
            mountain_point.append(point)                    # 경사도 기록 끝

    if mountain_point:                                 # 경사도가 존재하는 경우에만 실행
        minimum_point = mountain_point[0]                                       # 경사도최솟값 초기화
        for i in range(len(mountain_point)):
            if mountain_point[i] != 0 and mountain_point[i] < minimum_point:    # 경사도가 0이아니라면 최솟값으로 초기화
                minimum_point = mountain_point[i]

        result = 0
        for i in range(len(mountain_point)):
            if mountain_point[i] == minimum_point:                   # 경사도 최솟값을 갖는 경로들의 길이
                if mountain_lenth[i] > result:                          # 그중에서 가장 긴 경로를 result
                    result = mountain_lenth[i]


        if result != 1:
            print(f'#{tc} {result}')                                 #  출력
        else :
            print(f'#{tc} 0')                                       # 경로의 길이가 1일때
    else :
        print(f'#{tc} 0')                                           # 경사도가 존재하지 않을때
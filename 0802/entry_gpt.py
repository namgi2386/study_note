import sys
sys.stdin = open('z_e.txt','r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    entry_time_list = [int(input()) for _ in range(N)]
    
    left_time = 0 # 최적시간계산을 위한 최소시간
    right_time = min(entry_time_list) * M # 최적시간계산을 위한 최대시간
    
    result = right_time # 초기화
    
    while left_time <= right_time: # 최대최소시간이 교차될때까지
        mid_time = (left_time + right_time) // 2 # 중간부터

        total_people = 0 # 현재 지점에서 
        for entry_time in entry_time_list:
            total_people += mid_time // entry_time
            # 모든 사람을 심사할 수 있으면 더 이상 계산할 필요 없음
            if total_people >= M:
                break
        
        # mid_time 시간 동안 M명 이상을 심사할 수 있는지 여부에 따라 탐색 범위 조정
        if total_people >= M:
            result = mid_time
            right_time = mid_time - 1 # 중간값을 최댓값으로
        else:
            left_time = mid_time + 1 # 중간값을 최솟값으로
    
    print(f'#{tc} {result}')
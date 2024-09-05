def min_time_assignment(Time):
    N = len(Time)  # 사람 수 (또는 작업 수)
    dp = [1] * (1 << N)
    dp[0] = 0  # 아무것도 할당하지 않았을 때는 시간 0

    for mask in range(1 << N):
        # i: 현재까지 할당된 작업의 개수 = 현재 할당할 사람의 인덱스
        i = bin(mask).count('1')  
        for j in range(N):
            if not (mask & (1 << j)):  # j번째 작업이 아직 할당되지 않은 경우
                # mask 상태에서 i번째 사람이 j번째 작업을 할당받을 때의 최소 시간 갱신
                dp[mask | (1 << j)] = max(dp[mask | (1 << j)], dp[mask] * (Time[i][j]))

    return dp[(1 << N) - 1]  # 모든 작업이 할당된 상태에서의 최소 시간

# 예시 입력
Time = [
    [13, 0, 50],  # 첫 번째 사람
    [12, 70, 90],  # 두 번째 사람
    [25, 60, 100],  # 세 번째 사람
]





# 최소 작업 시간 계산
result = min_time_assignment(Time)
print(result)

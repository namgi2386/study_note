def min_time_assignment(Time):
    N = len(Time)  
    dp = [1] * (1 << N)
    dp[0] = 0  

    for mask in range(1 << N):
        i = bin(mask).count('1')  
        for j in range(N):
            if not (mask & (1 << j)):  
                dp[mask | (1 << j)] = max(dp[mask | (1 << j)], dp[mask] * Time[i][j])

    return dp[(1 << N) - 1]  # 모든 작업이 할당된 상태에서의 최소 시간

# 예시 입력
Time = [
    [0, 0,0,0],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 8, 4]
]

# 최소 작업 시간 계산
result = min_time_assignment(Time)
print(result)

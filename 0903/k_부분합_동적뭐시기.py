for tc in range(1,int(input())+1):
    n = int(input())
    arr =[list(map(int,input().split())) for _ in range(n)]

    dp = [[0]*n for _ in range(n)]
    # dp[r][c] => (r,c)까지 오는데 최소합
    # r,c 기준 위쪽 왼쪽 중에 최소 골라서 더하기
    for r in range(n):
        for c in range(n):
            # r,c 위치로 올 수 있는 방법은
            # 위에서 혹은 왼쪽에서 올 수 있음
            if 0<=r-1 and 0<=c-1:
                dp[r][c] = min(dp[r-1][c] , dp[r][c-1]) + arr[r][c]
            # 위에서만 올수있음
            elif r-1 >= 0 and c-1 < 0:
                dp[r][c] = dp[r-1][c] +arr[r][c]
            elif r-1 <0 and c-1 >= 0:
                dp[r][c] = dp[r][c-1] + arr[r][c]
            elif r-1 <0 and c-1 <0:
                dp[r][c] = arr[r][c]
    # 반복이 끝나면 맨 오른쪽 아래 칸에 최소값이 있다.
    print(f'#{tc} {dp}')
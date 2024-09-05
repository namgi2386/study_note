import sys
sys.stdin = open('z3.txt' , 'r')
# 계산했던 문제는 다시계산하지 않는다
# 작은문제를 먼저 계산한 뒤 
# 큰문제를 계산할 때 다시 계산하지 않는다.

# i까지 진행했을때의 최소 충전 값을 알고 있다면, 이후에 다시 계산하지 않을 예정이다
# dfs -> 백트래킹 -> dp 

for tc in range(1,int(input())+1):
    n , *arr=list(map(int,input().split())) 
    
    dp = [n]*n
    # dp[i] = i 번까지 가는데 최소 충전 횟수
    dp[0] = 0

    for i in range(1,n):
        # 이전위치 + arr[이전위치] >= i 일때만 올수있다.
        # dp[i]
        for j in range(i):
            if j + arr[j] >= i:
                dp[i] = min(dp[i], dp[j]+1)
    
    print(f'#{tc} {dp[n-1]-1}')



# 우리가 구하는건 최댓값이라 중간에 어떠케 가지치기하즤?
# 확률을 곱하면 곱할 수록 작아짐.
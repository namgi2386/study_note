import sys
sys.stdin = open('z5.txt' , 'r')

# 경우의수 12딜검색
# 각 격우에 대해 3가지 경우의 수 ( 일 , 월 , 3개월)
# 곧, 3^12 가지의 경우의수 
# 적당함 >> 완전탐색 가능

def dfs(month , sum_cost):
    global result
    if month > 12:
        result = min(result , sum_cost)
        return
    
    dfs(month+1 , sum_cost + (days[month]* cost[0] ))
    dfs(month+1 ,sum_cost + cost[1])
    dfs(month+3 ,sum_cost + cost[2])
    dfs(month+12 ,sum_cost + cost[3])
    
for tc in range(1,int(input())+1):
    result = 1e9
    cost = list(map(int,input().split()))

    #인덱스 check!
    days = [0] + list(map(int,input().split()))
    dfs(1,0)
    print(f'#{tc} {result}')

# DP 
# 작은문제로 분할 가능해야함 
# 전체문제의 합 - 각달까지의 최소 금액들이 쌓여서 완성
# 각 달까지의 최소금액문제로 생각
# 뒤에 결과를 구할때 앞선 결과가 변치 않는다.

# for tc in range(1,int(input())+1):
#     cost = list(map(int,input().split()))
#     days = [0] + list(map(int,input().split()))
#     dp =[0]*13

#     for i in range(1,13):
#         dp[i] = min(dp[i-1]+(days[i]*cost[0]), dp[i-1]+cost[1] )

#         if i >3:
#             dp[i] = min(dp[i] , dp[i-3] + cost[2])
#     result = min(dp[12],cost[3])
#     print(f'#{tc} {result}')
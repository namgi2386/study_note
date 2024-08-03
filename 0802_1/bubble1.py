import sys
sys.stdin = open('input_bubble.txt','r')

T = int(input())
for tc in range(1,T+1):
    n , m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_bubble_pop = 0

    for i in range(n):
        for j in range(m):          ## 완전탐색
            count_point = arr[i][j]     # 현재 위치
            if i==0 and j==0 :          #좌상단 모서리일때
                count_point += arr[i+1][j] + arr[i][j+1]
            elif i==n-1 and j==0:       #좌하단 모서리일때
                count_point += arr[i-1][j] + arr[i][j+1]
            elif i==0 and j==m-1:       #우상단 모서리일때
                count_point += arr[i+1][j] + arr[i][j-1]
            elif i==n-1 and j==m-1:     #우하단 모서리일때
                count_point += arr[i-1][j] + arr[i][j-1]
            elif i==0 and 0<j<m-1: # 위쪽 사이드일때
                count_point += arr[i+1][j]+arr[i][j-1]+arr[i][j+1]
            elif j==0 and 0<i<n-1: # 왼쪽 사이드일때
                count_point += arr[i-1][j] + arr[i+1][j] + arr[i][j+1]
            elif i==n-1 and 0<j<m-1: # 아래쪽 사이드일때
                count_point += arr[i - 1][j] + arr[i][j-1] + arr[i][j + 1]
            elif j==m-1 and 0<i<n-1: # 오른쪽 사이드일때
                count_point += arr[i - 1][j] + arr[i + 1][j] + arr[i][j - 1]
            else:                   # 그 외 중앙 어딘가일때
                count_point += arr[i - 1][j] + arr[i + 1][j] + arr[i][j - 1] + arr[i][j + 1]
            
            if max_bubble_pop < count_point:    # 최댓값 갱신
                max_bubble_pop = count_point
    print(f'#{tc} {max_bubble_pop}')

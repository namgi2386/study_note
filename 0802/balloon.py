import sys
sys.stdin = open('z2.txt','r')

T = int(input())
for tc in range(1,T+1):
    n , m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_bubble_pop = 0
    for i in range(n):
        for j in range(m):
            count_point = arr[i][j]
            if i==0 and j==0 :
                count_point += arr[i+1][j] + arr[i][j+1]
            elif i==n-1 and j==0:
                count_point += arr[i-1][j] + arr[i][j+1]
            elif i==0 and j==m-1:
                count_point += arr[i+1][j] + arr[i][j-1]
            elif i==n-1 and j==m-1:
                count_point += arr[i-1][j] + arr[i][j-1]
            elif i==0 and 0<j<m-1: # 위
                count_point += arr[i+1][j]+arr[i][j-1]+arr[i][j+1]
            elif j==0 and 0<i<n-1: # 왼쪽
                count_point += arr[i-1][j] + arr[i+1][j] + arr[i][j+1]
            elif i==n-1 and 0<j<m-1: # 아래
                count_point += arr[i - 1][j] + arr[i][j-1] + arr[i][j + 1]
            elif j==m-1 and 0<i<n-1: # 오른쪽
                count_point += arr[i - 1][j] + arr[i + 1][j] + arr[i][j - 1]
            else:
                count_point += arr[i - 1][j] + arr[i + 1][j] + arr[i][j - 1] + arr[i][j + 1]
            if max_bubble_pop < count_point:
                max_bubble_pop = count_point
    print(f'#{tc} {max_bubble_pop}')

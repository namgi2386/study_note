T = int(input())
for tc in range(1,T +1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    result = arr[0][0] + arr[0][1] + arr[1][0] # 첫번째자리에서의 점수를 result로 초기화
    for i in range(n):
        for j in range(n):
            total_sum = arr[i][j] # 현재위치의 값
            if i+1 < n :                    # 각 위치의 옆 칸들에 대해 범위 밖인지 검사
                total_sum += arr[i+1][j] # 아래
            if i-1 >= 0 :
                total_sum += arr[i-1][j] # 위
            if j+1 < n:
                total_sum += arr[i][j+1] # 오른쪽
            if j-1 >= 0 :
                total_sum += arr[i][j-1] # 왼쪽

            if total_sum > result: # 갱신
                result = total_sum
    print(f'#{tc} {result}')
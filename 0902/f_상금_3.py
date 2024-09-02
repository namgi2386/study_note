import sys
sys.stdin = open('z1.txt' , 'r')

def my_func(t):                     # 시작시 t=0 인데, 재귀 할때마다 1씩 증가
    global result
    if t==m:                        # t = m 재귀횟수가 m회 = m번 숫자교환 진행
        result = max(result, int("".join(arr))) # 그때의 arr값들이 최댓값이라면 갱신
        return        
    
    for i in range(n-1):        # i번째와 j번째의 숫자 교환
        for j in range(i+1, n): #
            arr[i] , arr[j] = arr[j] , arr[i]

            num = int("".join(arr)) # 교환이후의 숫자를 기록
            if (t, num) not in visited:
                my_func(t+1)
                visited.append((t,num))

            arr[j] , arr[i] = arr[i] , arr[j]       # 교환했던거 되돌리기



T = int(input())
for tc in range(1,T + 1):
    num , m = map(int, input().split()) # num=32888 , m=2
    arr = list(str(num)) # arr = ['3','2','8','8','8']
    n = len(arr) # n = 5
    result = 0
    visited=[]  # 이미 나온 수 기록하여 중복제거

    my_func(0) # 0부터 실행
    print(f'#{tc} {result}')
import sys
sys.stdin = open('in.txt','r')

T = int(input())

for tc in range(1,T+1):
    n = 10

    count_zero = 0

    number_set = list(map(int,input().split()))

    # 원소 n개인 집합의 부분집합 갯수 1024개
    # 2^n 번 계산해야함
    # 2^n번 == 1 << n
    # 1부터 (공집합제거)
    for i in range(1, 1<<n) :      #i == 1~1024        1<<10 == 1024
        # i 번째 부분집합의 합이 0인지 확인
        ith_subset_sum = 0
        ith_subset = []

        # i 를 이진수로 바꿔서 생각해보자.
        # 이진수의 각 자릿수는 0or1
        # 1이면 그 자릿수에 있는 원소를 골랐다고 생각함
        # 0이면 그 자릿수에 있는 원소를 안 고름
        # 이진수의 1을 왼쪽으로 최대 n번 이동시키며 비트 & 연산을 사용함
        # 왼쪽으로 0 ~ n-1번까지 이동
        for j in range(n): # j == 0~ 9
            if i & (1<<j) : # 0 이 아닐때 0000000000  ~~~ 0000100101 ~~ 1111111111           0000000010  ~ 1000000000
                # i를 이진수로 만들었을때
                # j번 원소를 i번째 부분집합에 포함된것으로 생각하겠다.
                ith_subset_sum += number_set[j]    # number_set[j] == -20 -6 -13 3 -19 -9 19 -3 9 4
                ith_subset.append(number_set[j])


        if ith_subset_sum == 0:
            count_zero = 1
            print(ith_subset)

    print(f'#########{tc} ## {count_zero}')
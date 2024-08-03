import sys
sys.stdin = open('c.txt','r')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    num_list = list(map(int, input().split()))

    count_carrat = 0
    max_num = num_list[n-1]+1
    result = 0

    for idx in range(n-1,-1,-1):
        if num_list[idx] < max_num:
            max_num = num_list[idx]
            count_carrat +=1
        
        else:
            max_num = num_list[idx]
            count_carrat = 1
        
        if result < count_carrat:
            result = count_carrat
    print(f'#{tc} {result}')

        
        
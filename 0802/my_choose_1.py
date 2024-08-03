import sys
sys.stdin = open('input1.txt','r')

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    my_str = input().split('0')  
    
    #  입력값이 '0011001110' 일때, 
    # '0011001110'를 '0' 기준으로 split 하여 my_str변수에 담으면
    # '0'이 모두 제거됨

    # print(my_str) >>> ['', '', '11', '', '111', ''] 이런형태로 저장됨.
    # 여기서 하나씩 뽑아서 길이 비교

    count = 0

    for i in range(len(my_str)):
        if len(my_str[i]) > count:
            count = len(my_str[i])

    print(f'#{tc} {count}')
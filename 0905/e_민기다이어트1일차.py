import sys
sys.stdin = open('z4.txt' , 'r')


def f(dec):
    score =0
    calorie = 0
    for i in range(n):
        if dec & (1<<i):
            score += arr[i][0] # 점수
            calorie += arr[i][1] # 칼로리
    # print(m, bin(1<<4), bin(dec),score,calorie , arr[1])
    return (score , calorie)




for tc in range(1, int(input())+1):
    n , m = map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(n)]
    
    result = 0

    for i in range(1<<n):
        score , calorie = f(i)
        if calorie <= m:
            result = max(result , score)

    print(f'#{tc} {result}')

# 남기님 열심히하세요
# 그러다 제가 금방 따라잡아요
# 저 어제 두 문제 다 풀었습니닿ㅎㅎㅎㅎ
# 누구세요?
# 11 = 01011
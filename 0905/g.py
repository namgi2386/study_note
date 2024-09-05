import sys
sys.stdin = open('z3.txt' , 'r')

def bus(now,lev):
    global min_cnt
    # 가지치기?
    if lev > min_cnt:
        return
    # 종료 조건
    if now >= N-1:
        if min_cnt >= lev:
            min_cnt = lev
        return
    # 재귀 호출
    for i in range(1, charge[now]+1):
        bus(now+i,lev+1)


T = int(input())

for tc in range(1,T+1):

    charge = list(map(int,input().split()))
    N = charge.pop(0)

    # N = charge[0] # N의 길이

    min_cnt = 10000 # 최소한의 길이 저장할 변수

    bus(0,0)

    print(f'#{tc} {min_cnt-1}')
import sys
sys.stdin = open('z3.txt' , 'r')

def bus(now,lev):
    global min_cnt

    if lev > min_cnt:
        return

    if now == N-1:
        min_cnt = min(min_cnt , lev)
        return


    for i in range(charge[now],0,-1):
        if now+i<N and lev<min_cnt:
            bus(now+i,lev+1)

# 5 2 3 1 1

T = int(input())

for tc in range(1,T+1):

    charge = list(map(int,input().split()))

    N = charge[0] # N의 길이

    min_cnt = 10000 # 최소한의 길이 저장할 변수


    bus(1,0)

    print(f'#{tc} {min_cnt-1}')
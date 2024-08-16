import sys
sys.stdin =open('z1.txt','r')

def empty_date():
    e_counts = 0
    for i in range(7):
        if arr[i] == 0:
            e_counts += 1
        else:
            return e_counts

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))

    d = counts = 0
    while counts != n:
        if arr[d%7] == 1:
            counts += 1
        d += 1

    print(f'#{tc} {d-empty_date()}')
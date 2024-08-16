import sys
sys.stdin = open('z2.txt','r')

T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())

    t = 2*m+1
    if n%t > 0:
        result = n//t +1
    elif n%t == 0:
        result = n//t
    else:
        result = 1
    print(f'#{tc} {result}')

import sys
sys.stdin = open('z1.txt','r')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    m = n
    s = set()
    while len(s) < 10:
        for x in str(n):
            s.add(x)
        n += m 
    print(f'#{tc} {n-m}')
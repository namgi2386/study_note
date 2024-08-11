import sys
sys.stdin = open('z1.txt','r')

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    str1 = list(map(int, input().split()))
    str2 = list(map(int, input().split()))
    if n > m:
        n , m = m , n # n은짧은거
        str1 , str2 = str2 , str1 # str1은 짧은거

    result = 0
    for h in range(m-n+1):
        counts = 0
        for i in range(n):
            counts += str1[i] * str2[i+h]
        if counts > result:
            result = counts
    print(f'#{tc} {result}')
    
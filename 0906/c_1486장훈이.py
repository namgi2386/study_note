import sys
sys.stdin = open('z3.txt' , 'r')




for tc in range(1,int(input())+1):
    result = 1e9
    n,m = map(int , input().split())
    arr = list(map(int,input().split()))
    for dec in range(1<<n):
        summer = 0
        for i in range(n):
            if dec & (1<<i):
                summer += arr[i]
        if summer - m >=0:
            result = min(result , summer-m)
    print(f'#{tc} {result}')
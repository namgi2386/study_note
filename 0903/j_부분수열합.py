import sys
sys.stdin = open('z3.txt' ,'r')

for tc in range(1,int(input())+1):
    n , m = map(int, input().split())
    arr =list(map(int, input().split()))
    counts = 0

    for num in range(1<<n):
        s=[]
        for i in range(n):
            hello =0
            if hello > m:
                break
            if num & (1<<i):
                hello += arr[i]

        if hello==m:
            counts += 1
    print(f'#{tc} {counts}')


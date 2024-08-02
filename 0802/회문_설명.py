T = int(input())
for tc in range(1,T+1):
    n,m = map(int, input().split())
    text = [list(input()) for _ in range(n)]

    result =""

    for i in range(n):
        for j in range(n-m+1):
            for k in range(m//2):
                pass
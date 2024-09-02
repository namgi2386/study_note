for tc in range(1,int(input())+1):
    n = int(input())
    counts = 0
    for i in range(32):
        if n & (1<<i):
            counts +=1
    print(f'#{tc} {counts}')
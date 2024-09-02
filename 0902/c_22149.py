for tc in range(1,int(input())+1):
    n = int(input())
    lst = list(map(int,input().split()))
    result = lst[0]
    for i in range(1,n):
        result = result ^ lst[i]

    print(f'#{tc} {result}')
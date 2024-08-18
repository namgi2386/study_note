def candy_count():
    candy = list(map(int,input().split())) # 3 5 5

    l = len(candy) # 3
    min_eat = 0
    candy.clear()
    for i in range(l-1, 0, -1):
        if candy[i] <= candy[i - 1]:
            min_eat += candy[i - 1] - candy[i] + 1
            candy[i - 1] = candy[i] - 1
        if candy[i - 1] <= 0:
            return -1
    return min_eat





T =int(input())
for tc in range(1,T+1):
    result = candy_count()
    print(f'#{tc} {result}')
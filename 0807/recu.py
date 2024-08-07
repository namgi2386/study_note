T = int(input())
for tc in range(1,T+1):
    num = int(input())
    a = num//20
    n = num//10
    arr = [1]*(n+2)
    for i in range(1,n+2):
        arr[i] = arr[i-1]*i
    # for j in range(a+1):
    #     (n-j)!/(n-2j)!*(2**j)
    result = 0
    for j in range(a+1):
        number = arr[n-j]/(arr[n-2j]*(2**j))
        result += number
    print(f'{tc} {result}')
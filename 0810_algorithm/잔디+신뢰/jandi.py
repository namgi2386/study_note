T = int(input())
for tc in range(1,T+1):
    arr = list(input())
    n = len(arr)
    counts = 0
    for i in range(n-1):
        if arr[i] == '(' and arr[i+1] == ')':
            arr[i] , arr[i+1] = 0 , 0
            counts += 1
    for i in range(n):
        if arr[i] == '(' or arr[i] == ')' :
            counts += 1
    print(f'#{tc} {counts}')
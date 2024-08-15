def party():
    sum_arr = arr
    counts = 0
    for i in range(n-1):
        sum_arr[i+1] += sum_arr[i]
        if sum_arr[i] < i+1 :
            sum_arr[i+1] += ((i+1)-sum_arr[i])
            counts += ((i+1)-sum_arr[i])
    return counts

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input()))
    n = len(arr)
    result = party()
    print(f'#{tc} {result}')






T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input()))
    n = len(arr)

    sum_arr = arr
    counts = 0
    for i in range(n-1):
        sum_arr[i+1] += sum_arr[i]

        if sum_arr[i] < i+1 :
            sum_arr[i+1] += ((i+1)-sum_arr[i])
            counts += ((i+1)-sum_arr[i])
    
    result = counts
    print(f'#{tc} {result}')

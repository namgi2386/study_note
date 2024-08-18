def stick():
    s= [arr[0]]
    prev = arr[0]
    counts = 0
    for i in range(1, len(arr)):
        if arr[i] == '(':
            s.append(arr[i])
        elif arr[i] == ')' and prev == '(':
            s.pop()
            counts += len(s)
        elif arr[i] == ')' and prev == ')':
            s.pop()
            counts += 1
        prev = arr[i]
    return counts

T = int(input())
for tc in range(1,T+1):
    arr= list(input())
    result = stick()
    print(f'#{tc} {result}')
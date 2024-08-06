T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    idx = 0
    arr = []
    while idx != N:
        arr.append([1] * (idx + 1))
        idx += 1

    temp = 3
    while N >= temp:
        for i in range(1, temp - 1):
            arr[temp - 1][i] = arr[temp - 2][i - 1] + arr[temp - 2][i]
        temp += 1
    print(f"#{tc}")
    for i in arr:
        a = " ".join(map(str, i))
        print(a)
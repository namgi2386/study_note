def find(num, k, lw, rw, ld, rd):
    global cnt
    if (lw < rw):
        return 0
    elif (num == k):
        return 1
    elif (d[ld][rd] != -1):
        return d[ld][rd]
    else:
        counts = 0
        for i in range(k):
            if (u[i] == 0):
                u[i] = 1
                p[num] = i
                counts += find(num + 1, k, lw + arr[i], rw, ld + (1 << i), rd)
                counts += find(num + 1, k, lw, rw + arr[i], ld, rd + (1 << i))
                u[i] = 0
        d[ld][rd] = counts
        return counts


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    p = [0] * N
    u = [0] * N

    d = [[-1] * (2 ** N) for i in range(2 ** N)]
    cnt = find(0, N, 0, 0, 0, 0)
    print(f'#{tc} {cnt}')
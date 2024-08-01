T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for k in range(4):
        for i in range(n - 1):
            for j in range(n - 1):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n
                    arr[ni][nj] = 'g'

    pi , pj = 1,1
    for d in range(4):
        ni = pi + di[d]
        nj = pj + dj[d]
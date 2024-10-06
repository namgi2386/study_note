import sys

sys.stdin = open("z3.txt", "r")


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n


def dfs(r, c, cut, cnt, d):
    global result
    if cnt > result:
        return

    if field[r][c] == "T":
        # 나문데 자를 수 없으면 리턴
        if not cut:
            return
        else:
            cut -= 1
    # 도착했을 때
    if r==3 and c==0 and cnt<10:
        for i in range(n):
            print(visited[i])
        print(tc , cnt , cut)
        print()

    if field[r][c] == "Y":
        if cnt < result:
            result = cnt
            # for i in range(n):
            #     print(visited[i])
            # print(result , cut)
            # print()
        return


    for x in range(4):
        # 우회전 좌회전
        if x == 1 or x == 3:
            d = (d + x) % 4
            nr = r + delta[d][0]
            nc = c + delta[d][1]

            if is_valid(nr, nc) and not visited[nr][nc]:
                visited[nr][nc] = 1
                dfs(nr, nc, cut, cnt + 2, d)
                visited[nr][nc] = 0
            # cnt += 1
        # 유턴
        elif x == 2:
            # cnt += 2
            d = (d + x) % 4
            nr = r + delta[d][0]
            nc = c + delta[d][1]

            if is_valid(nr, nc) and not visited[nr][nc]:
                visited[nr][nc] = 1
                dfs(nr, nc, cut, cnt + 3, d)
                visited[nr][nc] = 0
        else:
            # 변경된 방향
            # d = (d + x) % 4
            nr = r + delta[d][0]
            nc = c + delta[d][1]

            if is_valid(nr, nc) and not visited[nr][nc]:
                visited[nr][nc] = 1
                dfs(nr, nc, cut, cnt + 1, d)
                visited[nr][nc] = 0


# 상 우 하 좌
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    field = [input() for _ in range(n)]
    start_check = 0
    result = 1e9
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        if start_check != 0:  # 시작지점 찾았으면 break
            break
        for j in range(n):
            # 시작점이면
            if field[i][j] == "X":
                start_check = (i, j)  # 시작지점 체크
                visited[i][j] = 1
                break

    dfs(start_check[0], start_check[1], k, 0, 0)

    print(f"#{tc}", result)
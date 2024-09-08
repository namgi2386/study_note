import sys

sys.stdin = open("z4.txt", "r")

dr = [1, 1, -1, -1] #좌하단부터 반시계방향
dc = [-1, 1, 1, -1]

# dr = [1, 1, -1, -1]
# dc = [1, -1, -1, 1]# 안됨


def find_path(sr,sc):
    visited = [0] * 101

    r, c = sr, sc # 탐색의 시작지점
    for d in range(4): # d == 0 1 2 3 == 왼 오 왼 오
        if d%2 :
            l = right
        else: l = left

        for _ in range(l):
            r += dr[d]
            c += dc[d]
            if not visited[arr[r][c]]: # 한쪽 방향으로 이동하며 지나온 숫자들 기록
                visited[arr[r][c]] = 1
            # 먹은적 있으면 그만
            else:
                break
        else:
            # 반복 잘 돌았으면 계속
            continue
        # 아니면 그만
        break
    else:
        # 반복 잘 돌았으면 최대 길이 완성
        return total_length * 2

    return -1



for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    result = -1
    for total_length in range(n - 1, 1, -1): # 최소2 최대 n -1

        for left in range(1, total_length):
            right = total_length - left

            for i in range(n - total_length):
                for j in range(left, n - right):
                    ans = find_path(i,j)
        result = max(result , ans)

    print(f"#{tc} {result}")

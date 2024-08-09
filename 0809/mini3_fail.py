import sys
sys.stdin = open('z1.txt','r')

# N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)]

def make_perm(idx , selected , result , n):
    global minimamba

    if sum(result) > minimamba:
        return

    # 종료조건
    if idx == n:
        if minimamba > sum(result):
            minimamba = sum(result)

        return

    for i in range(n):
        if selected[i] == 0:
            selected[i] = 1
            result.append(lst[idx][i])
            make_perm(idx+1 , selected , result , n )

            selected[i] = 0
            result.pop()

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    minimamba = 100000000000000
    lst = [list(map(int, input().split())) for _ in range(N)]
    make_perm(0,[0]*N , [] , N)
    print(minimamba)

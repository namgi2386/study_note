import sys
sys.stdin = open('z2.txt','r')

T = int(input())
for tc in range(1,T+1):
    r,c = map(int,input().split())
    arr = [[]*c for _ in range(r)]

    for i in range(r):
        arr[i].extend(input())
        for j in range(c):
            if arr[i][j] in '<>^v':
                ti, tj = i , j
    
    n = int(input())
    moving_sign = input()

    for i in range(n):
        if moving_sign[i] == 'U' :
            arr[ti][tj] = '^'
            if ti > 0 and arr[ti-1][tj] == '.':
                arr[ti][tj] = '.'
                ti -= 1
                arr[ti][tj] = '^'

        elif moving_sign[i] == 'D':
            arr[ti][tj] = 'v'
            if ti < r-1 and arr[ti+1][tj] == '.':
                arr[ti][tj] = '.'
                ti += 1
                arr[ti][tj] = 'v'

        elif moving_sign[i] == 'L':
            arr[ti][tj] = '<'
            if tj > 0 and arr[ti][tj-1] == '.':
                arr[ti][tj] = '.'
                tj -= 1
                arr[ti][tj] = '<'

        elif moving_sign[i] == 'R':
            arr[ti][tj] = '>'
            if tj < c-1 and arr[ti][tj+1] == '.':
                arr[ti][tj] = '.'
                tj += 1
                arr[ti][tj] = '>'

        elif moving_sign[i] == 'S':
            if arr[ti][tj] == '^' :
                for h in range(ti-1,-1,-1):
                    if arr[h][tj] == '#':
                        break
                    if arr[h][tj] == '*':
                        arr[h][tj] = '.'
                        break

            if arr[ti][tj] == 'v' :
                for h in range(ti+1,r):
                    if arr[h][tj] == '#':
                        break
                    if arr[h][tj] == '*':
                        arr[h][tj] = '.'
                        break

            if arr[ti][tj] == '<' :
                for h in range(tj-1,-1,-1):
                    if arr[ti][h] == '#':
                        break
                    if arr[ti][h] == '*':
                        arr[ti][h] = '.'
                        break

            if arr[ti][tj] == '>' :
                for h in range(tj+1,c):
                    if arr[ti][h] == '#':
                        break
                    if arr[ti][h] == '*':
                        arr[ti][h] = '.'
                        break

    print(f'#{tc}',end=" ")
    for i in range(r):
        print("".join(arr[i]))

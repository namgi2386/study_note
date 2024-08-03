import sys
sys.stdin = open('z.txt','r')

T = int(input())
for tc in range(1,T+1):
    n , m = map(int,input().split())
    arr = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if j + m <= n:
                if arr[i][j] == arr[i][j+m-1]:
                    count_r =0
                    for k in range(m):
                        count_r += 1
                        if arr[i][j+k] != arr[i][j+m-1-k]:
                            break
                    if count_r == m:
                        result = [i,j,'r']
                        break

            if i + m <= n :
                if arr[i][j] == arr[i+m-1][j]:
                    count_c = 0
                    for k in range(m):
                        count_c += 1
                        if arr[i+k][j] != arr[i+m-1-k][j]:
                            break
                    if count_c == m:
                        result = [i,j,'c']
                        break
    if result[2] == 'r':
        i = result[0]
        j = result[1]
        print(f'#{tc} ',end="")
        for h in range(m):
            print(arr[i][j+h],end="")

    if result[2] == 'c':
        i = result[0]
        j = result[1]
        print(f'#{tc} ',end="")
        for h in range(m):
            pass
            print(arr[i+h][j] , end="")
    print()



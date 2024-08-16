import sys
sys.stdin = open('z1.txt','r')

def ww():
    for i in range(n):
        for j in range(m):
            if arr[i][j] in '#.':
                return (i,j ,arr[i][j])
    return (0,0,0)

def who_r_u():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '#':
                if (i+j)%2 ==0 :
                    for k in range(0,n,2):
                        for l in range(0,m,2):
                            if arr[k][l] == '.':
                                return 'impossible'
                    for k in range(1,n,2):
                        for l in range(1,m,2):
                            if arr[k][l] == '#':
                                return 'impossible'
                else:
                    for k in range(1,n,2):
                        for l in range(1,m,2):
                            if arr[k][l] == '.':
                                return 'impossible'
                    for k in range(0,n,2):
                        for l in range(0,m,2):
                            if arr[k][l] == '#':
                                return 'impossible'
            if arr[i][j] == '.':
                if (i+j)%2 ==0 :
                    for k in range(0,n,2):
                        for l in range(0,m,2):
                            if arr[k][l] == '#':
                                return 'impossible'
                    for k in range(1,n,2):
                        for l in range(1,m,2):
                            if arr[k][l] == '.':
                                return 'impossible'
                else:
                    for k in range(1,n,2):
                        for l in range(1,m,2):
                            if arr[k][l] == '#':
                                return 'impossible'
                    for k in range(0,n,2):
                        for l in range(0,m,2):
                            if arr[k][l] == '.':
                                return 'impossible'
    return 'possible'

T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    result = who_r_u()
    print(f'#{tc} {result}')

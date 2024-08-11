import sys
sys.stdin = open('z2.txt','r')

def russia(n,m,matrix):
    # n=4행 m=5열 상태의 matrix
    result = m*n

    wcounts = 0
    for w in range(n-2): # n-2 == 2 즉 w = 0,1가능
        for h in range(m):
            if matrix[w][h] != 'W':
                wcounts += 1
        bcounts = 0
        for b in range(w+1,n-1):
            for h in range(m):
                if matrix[b][h] != 'B':
                    bcounts += 1
            rcounts = 0
            for r in range(b+1,n):
                for h in range(m):
                    if matrix[r][h] != 'R':
                        rcounts += 1
            all_counts = wcounts + bcounts + rcounts
            if result > all_counts:
                result = all_counts
    return result


T = int(input())
for tc in range(1,T+1):
    n , m = map(int,input().split())
    matrix = [list(input()) for _ in range(n)]
    result = russia(n,m,matrix)
    print(f'#{tc} {result}')

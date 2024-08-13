import sys
sys.stdin = open('z1.txt' , 'r')

T = int(input())

def fly(matrix):
    
    result = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            get_fly = 0
            for h in range(m):
                for k in range(m):
                    get_fly += matrix[i+h][j+k]
            
            if get_fly > result:
                result = get_fly
    return result

for tc in range(1,T+1):
    n,m = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]

    result = fly(matrix)
    print(f'#{tc} {result}')
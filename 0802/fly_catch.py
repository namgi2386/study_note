import sys
sys.stdin = open("i_f.txt", "r")

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())

    matrix = [list(map(int,input().split())) for _ in range(N)]

    result = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for i_f in range(M):
                for j_f in range(M):
                    total += matrix[i + i_f ][j + j_f]
            
            if total >= result:
                result = total
    
    print(f"#{tc} {result}")
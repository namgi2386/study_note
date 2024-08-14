import sys
sys.stdin = open('z2.txt', 'r')

T = int(input())

def supernova(matrix):
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    matrix_c = []
    for a in range(9):
        lic = []
        for b in range(9):
            lic.append(matrix[b][a])
        matrix_c.append(lic)

    for i in range(9):
        for j in range(9):
            if check_list[j] not in matrix[i]:
                return 0
            if check_list[j] not in matrix_c[i]:
                return 0

    for i in [1,4,7]:
        for j in [1,4,7]:
            li = [matrix[i][j]]
            for h in range(8):
                li.append(matrix[i+dr[h]][j+dc[h]])
            for e in range(9):
                if check_list[e] not in li:
                    return 0
    return 1

for tc in range(1,T+1):
    matrix = [list(map(int,input().split())) for _ in range(9)]
    check_list = [1,2,3,4,5,6,7,8,9]
    print(f'#{tc} {supernova(matrix)}')

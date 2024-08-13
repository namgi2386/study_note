T = int(input())

def supernova(matrix):

    for i in range(9):
        if check_list[i] not in matrix[i]:
            return 0
    
            pass

    return 1

for tc in range(1,T+1):
    matrix = [list(map(int,input().split())) for _ in range(9)]
    check_list = '123456789'
    print(f'#{tc} {supernova(matrix)}')

    



arr2 = [[0]*3 for i in range(6)]

for i in range(6):
    pass
    #print(*arr2[i])


for i in range(6):
    for j in range(3):
        pass
        #print(arr2[i][j], end=" ")
    #print()

arr = [[1,2,3],[4,5,6]]
print(len(arr)) # 행수
print(len(arr[0])) # 열수

arr = [[0]*3]*2
print(arr)  # [[0,0,0],[0,0,0]]
arr[0][0] = 1
print(arr)  # [[1,0,0],[1,0,0]]
print()

arr = [[1,2,3],[4,5,6,],[7,8,9]]
n = 3

for i in range(n):          # 열먼저
    rs = 0
    cs = 0
    for j in range(n):      # 행먼저
        rs += arr[i][j]      # 각 행의 합
        cs += arr[ j ][ i ]      # 각 열의 합
    print(f'#{i}행의 합 == {rs}')
    print(f'#{i}열의 합 == {cs}')
    print()


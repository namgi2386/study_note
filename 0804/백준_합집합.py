
arr = [ list(map(int, input().split())) for _ in range(4) ]
n = 10
zero_arr = [[0]*n for _ in range(n) ]

for k in range(4):
    s_x = arr[k][0] -1
    s_y = arr[k][1] -1
    e_x = arr[k][2] -1
    e_y = arr[k][3] -1
    for x in range(s_x,e_x+1):
        for y in range(s_y,e_y+1):
            zero_arr[x][y] = 1 
    if k == 3:
        for i in range(n):
            print(zero_arr[i])
counts = 0
for i in range(0,n-1,2):
    for j in range(0,n-1,2):
        if zero_arr[i][j] == 1 and zero_arr[i+1][j+1]==1 and zero_arr[i+1][j]==1 and zero_arr[i][j+1]==1 :
            counts += 1
print(counts)

arr = [ list(map(int, input().split())) for _ in range(4) ]

zero_arr = [[0]*100 for _ in range(100) ]

for k in range(4):

    for i in range(arr[k][0] , arr[k][2]):
        for j in range(arr[k][1] , arr[k][3]):
            zero_arr[i][j] = 1

counts = 0
for i in range(100):
    for j in range(100):
        if zero_arr[i][j] == 1:
            counts += 1
print(counts)
garo , sero  = map(int, input().split())
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n) ]
l = len(arr)

lst_garo = [0,garo]
lst_sero = [0,sero]

for i in range(l):
    if arr[i][0]: lst_garo.append(arr[i][1])
    else: lst_sero.append(arr[i][1])

lst_garo.sort()
lst_sero.sort()
print(lst_garo) # [0, 4, 10]
print(lst_sero) # [0, 2, 3, 8]

max_garo = 0
max_sero = 0
for i in range(len(lst_garo)-1):
    sep = lst_garo[i+1]-lst_garo[i]
    if sep > max_garo :
        max_garo = sep
for i in range(len(lst_sero)-1):
    sep = lst_sero[i+1]-lst_sero[i]
    if sep > max_sero :
        max_sero = sep
print(max_garo*max_sero)





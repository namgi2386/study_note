date,sep=map(int,input().split())
arr = list(map(int,input().split()))


max_num = 0
for h in range(sep):
    max_num += arr[h]
num = max_num

for i in range(1, date-sep+1):
    dif = arr[i + sep -1] - arr[i-1]
    num += dif
    if  max_num < num : max_num = num

print(max_num)
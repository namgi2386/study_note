date,sep=map(int,input().split())
arr = list(map(int,input().split()))


max_num = 0
for h in range(sep):
    max_num += arr[h]


for i in range(1, date-sep+1):
    num = 0
    for h in range(sep):
        num += arr[i+h]
    if max_num < num:
        max_num = num
print(max_num)
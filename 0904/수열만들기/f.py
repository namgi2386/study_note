
arr = [1,2,1,2]

n=4
cnt = 0
for idx in range(1<<n): # idx = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
    s=[]
    for i in range(n): # 0,1,2,3
        if idx & (1<<i):   # 
            s.append(i)
    
    if len(s) >= 1:
        sub_sum = 0
        for j in s:
            sub_sum += arr[j]
        if sub_sum == 3:
            cnt += 1

print(cnt)


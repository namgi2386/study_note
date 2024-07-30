n = 5
lst = [55,7,78,12,42]

for i in range(n-1,0,-1):
    for j in range(i):
        if lst[j] > lst[j+1]:
            lst[j] , lst[j+1] = lst[j+1] , lst[j]
print(lst)
hax=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
arr = list(input())
n = len(arr)
re= ""
for i in range(n):
    h = hax.index(arr[i])
    r = ""
    for j in range(4):
        if h & (1<<j):
            r = '1' + r
        else:
            r = '0' + r
    
    re += r
result = []
print(re)
for i in range(4*n//7):
    result.append(int(re[7*i:7*i+7],2))
result.append(int(re[(4*n//7)*7:],2))
print(*result)




n = 7

arr = []
for w in range(0,n-2): # 총 n=7칸이며 , 가운데 n-2=5칸이라고하면 w 는 0~4칸
    for t in range(1,n-1-w): # w부터 끝까지 가능해야함 
        for r in range(n-2-w-t,n-1-w-t): # w+t부터 끝까지
            arr.append([w,t,r])
print(arr)

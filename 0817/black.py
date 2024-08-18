def black(t):
    global result
    if len(s) == 3:
        ss = 0
        for i in range(3):
            ss += arr[s[i]]
        if m >= ss :
            result = min(result,m-ss)
        return
    for i in range(t,n):
        if i not in s:
            s.append(i)
            black(i+1)
            s.pop()

n,m=map(int,input().split())
result = m
s=[]
arr = list(map(int,input().split()))
black(0)
print(m - result)

                


    
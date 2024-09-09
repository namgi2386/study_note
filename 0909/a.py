n,m=map(int,input().split())

def f(lev , s,t):
    if lev==m:
        print(*s)
        return
    for i in range(t,n+1):
        if i not in s:
            s.append(i)
            f(lev+1 , s,i+1)
            s.pop()

f(0,[],1)
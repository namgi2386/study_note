def f(lev,a,b):
    if a in v or b in v:
        return
    if len(a)>n//2 or len(b)>n//2:
        return
    if lev==n:
        v.append(a)
        v.append(b)
        print(a,b)
        return
    f(lev+1,a+[lev],b)
    f(lev+1,a,b+[lev])

v =[]
n =4
f(0,[],[])



def f(lev,a,b):
    if a in v or b in v:
        return
    if len(a)>n//2 or len(b)>n//2:
        return
    if lev==n:
        v.append(a)
        v.append(b)
        print(a,b)
        return
    f(lev+1,a+[lev],b)
    f(lev+1,a,b+[lev])

v =[]
n =4
f(0,[],[])
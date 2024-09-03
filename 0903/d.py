def dice(t , p):
    if len(s)==3:
        print(s)
        return

    for i in range(p,7):
        s.append(i)
        dice(t+1 , i)
        s.pop()

s=[]
dice(0,1)



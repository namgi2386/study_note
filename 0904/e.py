def a(t):
    global cnt
    if len(s)==m:
        print(s)
        return
    for i in range(t,n+1):
        s.append(i)
        a(i)
        s.pop()





n=3
m=2
cnt = 0
s=[]
a(1)

'''
[1, 1]
[1, 2]
[1, 3]
[2, 2]
[2, 3]
[3, 3]
'''
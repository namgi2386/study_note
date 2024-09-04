def a():
    if len(s) == m:
        print(s)
        return
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            a()
            s.pop()


n=3
m=2
s=[]
a()

'''
[1, 2]
[1, 3]
[2, 1]
[2, 3]
[3, 1]
[3, 2]
'''
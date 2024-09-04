def a():
    if len(s)==n:
        print(s)
        return
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            a()
            s.pop()


n=3
s=[]
a()

'''
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
'''
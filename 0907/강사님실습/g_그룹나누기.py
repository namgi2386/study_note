

def f(i,a,b,c):
    if len(a)>n//3+1 or len(b)>n//3+1 or len(c)>n//3+1:
        return
    
    if i==n and a and b and c:
        print(a,b,c)
    f(i+1,a+[i],b,c)
    f(i+1,a,b+[i],c)
    f(i+1,a,b,c+[i])

n = 4
f(0,[],[],[])
print('--'*10)
'''
[0, 1] [2] [3]
[0, 1] [3] [2]
[0, 2] [1] [3]
[0] [1, 2] [3]
[0, 3] [1] [2]
[0] [1, 3] [2]
[0] [1] [2, 3]
[0, 2] [3] [1]
[0, 3] [2] [1]
[0] [2, 3] [1]
[0] [2] [1, 3]
'''
def g(i,a,b,c):
    if len(a)>n//3 or len(b)>n//3 or len(c)>n//3:
        return
    
    if i==n :
        print(a,b,c)
    g(i+1,a+[i],b,c)
    g(i+1,a,b+[i],c)
    g(i+1,a,b,c+[i])

n = 3
g(0,[],[],[])



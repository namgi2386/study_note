n = 10
for i in range(1,n+1):
    print(i , end=" ")
print()

e = 1
while e < 11 :
    print(e, end=" ")
    e += 1
print()
def you(n):
    if n == 10:
        return '10'
    return f'{n} {you(n+1)}'
print(you(1))

def myprint(j,n):
    if j > n:
        return
    print(j,end=" ")
    myprint(j+1,n)
    return
n=10
myprint(1,n)
print()

n = 5
arr = [[n*j+i for i in range(1,n+1)] for j in range(n)]

print()
n = 3
def myprint(t):
    global n
    if t==n*n+1 :
        return

    print(t, end=" ")
    if t == n*(t//n):
        print()
    myprint(t+1)

myprint(1)

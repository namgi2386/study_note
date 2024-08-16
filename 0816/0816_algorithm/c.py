n,m = map(int,input().split())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(f'{i} {j}')

s= []
def ee():
    if len(s) == m:
        print(*s)
        return

    for i in range(1,n+1):
        s.append(i)
        ee()
        s.pop()
ee()
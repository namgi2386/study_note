'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
'''
def f(q):
    while q:
        r,c = q.pop()
    for i in range(s_n):
        

m,n = map(int ,input().split())
arr =[list(map(int ,input().split())) for _ in range(n)]
start_point =[]
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            start_point.append((i,j))
s_n = len(start_point)
f(start_point)
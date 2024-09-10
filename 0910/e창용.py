import sys
sys.stdin = open('z3.txt','r')

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parents[root_x] = root_y

for tc in range(1,int(input())+1):
    n,m = map(int,input().split()) # 5 2
    parents = [i for i in range(n+1)]

    for _ in range(m):
        a,b = map(int,input().split())
        union(a,b)

    for i in range(1,n+1):
        find(i)

    s=set() # 중복제거하기
    for i in range(n+1):
        s.add(parents[i])

    print(f'#{tc} {len(s)-1}')


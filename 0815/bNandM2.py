def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1,n+1):
        if visited[i]:
            continue
        visited[i] = 1
        s.append(i)
        dfs()
        s.pop()
        visited[i] = 0

n , m = map(int,input().split())
s = []
visited = [0]*(n+1)

dfs()




def dfs2():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
n,m = list(map(int,input().split()))
s = []
dfs2()
def dfs():
    if len(s) == m:
        print(*s)
        return
    for i in range(1,n+1):
        if visited[i]:
            continue
        s.append(i)
        visited[i]=1
        dfs()
        s.pop()
        visited[i]=0
n,m = map(int,input().split())
s=[]
visited =[0]*(n+1)

dfs()

def BFS(G, v):
    # 준비과정
    visited = [0]*(n+1)
    queue=[]
    queue.append(v)
    visited[v] = 1

    # 탐색과정
    while queue:
        t = queue.pop(0)
        # visit(t)
        for i in G[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
n = 10
arr =[1,2]
v = 0
result = BFS(arr,v)
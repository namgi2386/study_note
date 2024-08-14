def bfs(s,v):
    visited = [0]*(v+1)
    q = []
    q.append(s)
    visited[s] = 1

    while q:
        t = q.pop(0)
        print(t)
        for w in adj_l[t]:
            if visited[w] == 0 :
                q.append(w)
                visited[w] = 1

v, e = map(int ,input().split())
arr = list(map(int , input().split()))
adj_l = [[] for _ in range(v+1) ]
for i in range(e):
    v1, v2 = arr[i*2] , arr[i*2 +1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)
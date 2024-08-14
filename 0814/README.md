> 어제 내용 이어서 진행
# Queueue 2

## 🐉BFS 너비우선탐색🐉

```python
def BFS(G, v):                      #
    # 준비과정
    visited = [0]*(n+1)             #visited = [ [0][0][0][0][0][0]...]
    queue = []                      #
    queue.append(v)                 # 시작지점 넣고 시작

    # 탐색과정
    while queue:                    #
        t = queue.pop(0)            # t = 방문할 노드
        if not visited[t]:          # 방문한적 없는 노드라면
            visited[t] = True       # 방문체크
            #visit(t)               #
            for i in G[t]:          # t와 연결된 노드 들에대하여
                if not visited[i]:  # 방문한적 없다면
                    queue.append(i) # 전부 큐에 넣기 (이따가 하나씩 뺄 예정)
n = 10
arr =[1,2]
v = 0
result = BFS(arr,v)
```

```python
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
```
```python
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
```
```python

def bfs(i,j,N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append([i,j])
    visited[i][j] = 1
    
    while q:
        ti,tj = q.pop(0)
        if maze[ti][tj] == 3:
            return visited[ti][tj] -1 -1
        for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            wi,wj = ti+di , tj + dj
            if 0<= wi<N and 0<= wj <N and maze[wi][wj] != 1 and visited[wi][wj] = 0:
                q.append([wi,wj])
                visited[wi][wj] =visited[wi][wj] + 1
    return -1

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i,j

N = int(input())
maze = [list(map(int , input().split())) for _ in range(N) ]
sti , stj = find_start(N)
ans = bfs(sti , stj , N)
```
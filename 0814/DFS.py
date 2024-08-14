from collections import deque

'''
정점의 개수 : V , 간선의 개수 : E
V = 7 ,E=8
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''

def bfs(G,v,N):
    # 중복방지를 위한 방문 배열
    visited = [0]*(N+1)
    # 방문할 곳을 기록할 큐
    q = deque() # q = deque([1,2,3]) 기본값넣고시작하기

    q.append(v)
    visited[v] = 1

    while q:
        now = q.popleft()

        #####################
        print(now, end=" ")
        #####################

        for next in G[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = visited[now]+1

V , E = map(int , input().split())
G =[[] for _ in range(V+1)]
for i in range(E):
    start , end = map(int , input().split())
    G[start].append(end)
    G[end].append(start)

bfs(G,1,V)
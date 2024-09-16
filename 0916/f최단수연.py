import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    pq = []
    heappush(pq,(0,start)) # pq안에 (0,start)를 distance를 기준으로 오름차순 삽입
    distance[start] = 0

    while pq:
        # 가장 최단거리인 노드에 대한 정보꺼내기
        dist, now = heappop(pq)
        if distance[now] < dist:
            continue # while로 돌아감

        # 현재 노드와 연결된 다른 인접한 노드 검사
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost

            # 다음 노드로 가는 데 더 많은 비용이 들면
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heappush(pq,(new_cost,next_node))


n,m = map(int,input().split()) # 정점의 개수, 간선의 개수
start = int(input())
graph = [[] for _ in range(n+1)] # 2차원 배열
# INF_num = 1e9 # 큰수
distance = [INF] * (n+1) # 누적거리를 저장할 그래프
for _ in range(m):
    a,b,w = map(int,input().split())
    graph[a].append((b,w)) # 가중치 있는 그래프

dijkstra(start)
for i in range(1,n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
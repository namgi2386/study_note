from heapq import heappush, heappop
import sys
sys.stdin = open('z2.txt' , 'r')

def dijkstra(start):
    heap =[]
    heappush(heap, (0,start))
    distance[start] = 0

    while heap:
        dist , now = heappop(heap)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist +cost

            if new_cost >= distance[next_node]:
                continue
            distance[next_node] = new_cost
            heappush(heap , (new_cost , next_node))


for tc in range(1,int(input())+1):
    n, m = map(int, input().split())
    start = 0
    graph = [[] for i in range(n+1)]
    INF = int(1e9)
    distance = [INF] * (n+1)
    
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a].append([b, w])

    dijkstra(start)

    print(f'{tc} {distance[-1]}')
    # 모든 노드로 가기 위한 최단 거리 출력
    # for i in range(n):
    #     # 도달할 수 없는 경우, 무한 출력
    #     if distance[i] == INF:
    #         print("INF", end=' ')
    #     else:
    #         print(distance[i], end=' ')
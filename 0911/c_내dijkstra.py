from heapq import heappush, heappop
import sys
sys.stdin = open('z1.txt' , 'r')

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


# for tc in range(1,int(input())+1):
n, m = map(int, input().split())
start = 0
graph = [[] for i in range(n)]
INF = int(1e9)
distance = [INF] * n

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(n):
    # 도달할 수 없는 경우, 무한 출력
    if distance[i] == INF:
        print("INF", end=' ')
    else:
        print(distance[i], end=' ')
'''
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''
from heapq import heappush, heappop
import sys
sys.stdin = open('z1.txt' , 'r')

def dijkstra(start):
    h =[]
    heappush(h, (0,start))
    visited[start] = 0

    while h:
        dist , now = heappop(h)
        if visited[now] >= dist:
            for next in arr[now]:
                next_node = next[0]

                new_cost = dist +next[1] # 누적합

                if new_cost < visited[next_node]:
                    visited[next_node] = new_cost
                    heappush(h , (new_cost , next_node))


# for tc in range(1,int(input())+1):
n, m = map(int, input().split())

arr = [[] for i in range(n)]
INF = 1e9
visited = [INF] * n

for _ in range(m):
    a, b, w = map(int, input().split())
    arr[a].append((b, w))

dijkstra(0)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(n):
    # 도달할 수 없는 경우, 무한 출력
    if visited[i] == INF:
        print("INF", end=' ')
    else:
        print(visited[i], end=' ')
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
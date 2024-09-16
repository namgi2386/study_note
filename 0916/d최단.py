import sys
sys.stdin = open('z1.txt' , 'r')

from heapq import heappop , heappush
def f(start):
    h =[]
    heappush(h , (0,start))
    visited[start] = 0

    while h:
        dist , now = heappop(h)
        if visited[now] >= dist:
            for next in arr[now]:
                next_node = next[0]
                new_cost = dist + next[1]
                if new_cost < visited[next_node]:
                    visited[next_node] = new_cost
                    heappush(h , (new_cost ,next_node))

n , m = map(int, input().split())
start = int(input())
arr = [[] for _ in range(n+1)]
min_num = 1e9
visited = [min_num]*(n+1)

for _ in range(m):
    a,b,w = map(int, input().split())
    arr[a].append((b,w))

f(1)
for i in range(1,n+1):
    if visited[i] == 1e9:
        print('INF')
    else:
        print(visited[i])
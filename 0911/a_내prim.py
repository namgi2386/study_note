from heapq import heappush , heappop

def prim(start):
    heap = list()
    visited = [0]*n

    sum_weight = 0

    heappush(heap, (0, start))

    while heap:
        weight ,  position = heappop(heap)

        if visited[position]:
            continue

        visited[position] = 1
        sum_weight += weight

        for next in range(n):
            if arr[position][next] == 0:
                continue
            if visited[next]:
                continue
            heappush(heap , (arr[position][next] , next))
    return sum_weight

n , m = map(int, input().split())
arr = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b,w = map(int, input().split())
    arr[a][b] = w
    arr[b][a] = w

print(f'최소비용 = {prim(0)}')
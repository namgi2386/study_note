from heapq import heappop , heappush

dr =[]
dc =[]

def djk():
    q = [(0,0,0)]
    distance[0][0] = 0

    while q:
        w,r,c = heappop(q)

        if distance[r][c] < w:
            continue
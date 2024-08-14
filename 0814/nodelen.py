from collections import deque
import sys
sys.stdin = open('z3.txt', 'r')

def noodle(sn,en):
    visited = [0]*(v+1)
    q= deque()
    q.append(sn)
    visited[sn] = 0
    while q:
        now = q.popleft()

        for x in arr[now]:
            if not visited[x]:
                q.append(x)
                visited[x] = visited[now]+1
                if x == en:
                    return visited[x]
    return 0

T = int(input())
for tc in range(1,T+1):
    v,e = map(int,input().split())
    arr=[[] for _ in range(v+1)]
    for i in range(e):
        sta,end =map(int,input().split())
        arr[sta].append(end)
        arr[end].append(sta)
    s , g = map(int,input().split())
    result = noodle(s,g)
    print(f'#{tc} {result}')
from collections import deque

def rabbit():
    lev = 0
    q = deque()
    q.append((n,lev)) 
    while q:
        num , cnt = q.popleft()
        if num == m: return cnt
        if 0< num<=limm and visited[num]:
            visited[num] = 0
            li = [(num+1,cnt+1),(num-1,cnt+1),(num-10,cnt+1),(num*2,cnt+1)]
            q.extend(li)

for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    limm = 1000020
    visited =[1]*limm
    print(f'#{tc} {rabbit()}')


from collections import deque
 
def f(i, N):        # i번 사람부터 무리를 탐색하는 함수
    visited[i] = 1
    for j in adj[i]:    # i와 아는 관계인 j가 속한 무리가 없으면
        if visited[j] == 0:
            f(j, N)
 
def bfs(i):      # 같은 무리의 사람을 모두 확인하는 탐색
    q = deque()     # 큐 생성
    q.append(i)     # 시작점 인큐
    visited[i] = 1  # 시작점 인큐 표시
    while q:        # 큐에 탐색할 정점이 남아있으면
        i = q.popleft()     # dequeue, 인접 순으로 디큐
        for j in adj[i]:     # 인접(같은 무리) 정점이
            if visited[j] == 0:      # 방문 전이면
                q.append(j)             # 인큐하고, 인큐표시
                visited[j] = visited[i] + 1
 
 
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 사람의 수 N, 서로를 알고 있는 사람의 관계 수 M
    adj = [[] for _ in range(N+1)]      # 1-N번 사람이 알고있는 관계를 표시하는 인접리스트
    for _ in range(M):
        a, b = map(int,input().split())
        adj[a].append(b)            # a-b 아는사이,  같은 관계는 반복해서 주어지지 않는다.
        adj[b].append(a)            # b-a 양방향인가?
 
    cnt = 0                         # 무리의 수
    visited = [0] * (N + 1)         # 관계가 확인된 사람
    for i in range(1, N+1):         # 모든사람의 관계 확인
        if visited[i] == 0:         # 아직 확인전이면(무리에 속하지 않은 사람이면)
            cnt += 1                # 새로운 무리 추가
            #f(i, N)
            bfs(i)
 
    print(f'#{tc} {cnt}')
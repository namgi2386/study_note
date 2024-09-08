from collections import deque

def bfs(N,M):
    ans = 0
    q = deque()# 큐 생성
    visited = [[-1]*M for _ in range(N)] # visited 생성
    for i in range(N): # 출발점(모든 물) 인덱스 인큐
        for j in range(M):
            if arr[i][j] == 'W':
                q.append([i,j])  # 출발점 인큐 표시
                visited[i][j] = 0 # 방문표시
    while q: # 탐색할 땅이 남아있으면
        i,j = q.popleft() # 인접할 땅을 조사할 격자칸 인덱스 디큐
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 상하좌우
            ni,nj = i+di, j+dj
            # 유효한 인덱스이고 방문하지 않은 곳이면
            if 0<=ni<N and 0<=nj<M and visited[ni][nj]==-1:
                q.append((ni,nj)) # 리스트로 넣으면 시간 더 걸림
                visited[ni][nj] = visited[i][j] + 1
                ans += visited[ni][nj]

    return ans

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split()) # N*M배열
    arr = [input() for _ in range(N)]
    
    ans = bfs(N,M) # 모든 땅에서 물까지의 최단거리
    print(f'{tc} {ans}')

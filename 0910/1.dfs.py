# page25. 연습문제1
import sys
sys.stdin = open("graph.txt", "r")

# 시작점 : 1번 노드
# 끝점 : 모든노드 방문시
def dfs(node):
    print(node, end=' ')  # 현재 노드 출력

    # 갈 수 있는 노드들을 탐색
    for next_node in graph[node][::-1]: # 큰수부터 탐색하기
        if visited[next_node]: # 방문한적있을때
            continue

        visited[next_node] = 1 # 첫방문시 방문기록
        dfs(next_node)         # 재귀호출이 for문 속에있기에 dfs깊게이동


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]


visited = [0] * (N + 1) # n+1번 : 0번 인덱스를 버림
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s) # 양방향그래프

visited[1] = 1 # 출발지 방문처리
dfs(1)

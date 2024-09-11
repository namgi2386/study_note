# 두가지 순회방법 BFS, DFS

# DFS
# 위상정렬은 하나의 선형 순서가 결과로 나온다
# 간선의 방향성을 유지하면서 그래프의 모든 정점을 나열
# N개의 정점
# [v1, v2, v3, ... vN] 까지의 정점에 대하여
# 임의의 간선 (vi ,vj)에 대하여 i<j 가 성립해야 한다.
# 비순환그래프에서만 가능하다.
# 결과가 유일하지 않을 수 있다.
    # both of (a->b) , (c->b) is available
    # to make b , have to make a and c
    # in this point order of (a and c) can be changed
# 깊이 우선 탐색 기반의 위상정렬
# DFS(깊이 우선 탐색)을 수행하면서 각 노드가 처리되는 순서를
# 스택에 저장

# 모든 노드를 방문한 다음에 스택의 내용을 역순으로 정렬하면 결과 도출

# 1. 방문하지 않은 모든 정점에 대해서 DFS 실행
# 2. 어떤 정점에 대해서 그 정점과 인접한 모든 정점을 방문한 후에 스택에 추가
    # 현재 정점에서 갈수있는 모든정점을 다탬색한 후 현재 정점을 스택에 추가
# 3. 스택을 역순으로 정렬하면 위상정렬이 된다.

#그래프
# G =[[] for _ in range(5)]
# # 방문정점 체크
# visited = set()
# stack = [] #
#
# def dfs(node):
#     visited.add(node)
#
#     for next_node in G[node]:
#         if next_node not in visited:
#             dfs(next_node)
#
#     stack.append(node)
#
# print(stack[::-1])


def dfs(node , visited , stack):
    visited.add(node)
    for next in arr[node]:
        if next not in visited:
            dfs(next,visited,stack)
    stack.append(node)

for tc in range(1,11):
    n,m = map(int,input().split())
    edges = list(map(int,input().split()))

    arr =[[] for _ in range(n+1)]
    for i in range(m):
        a = edges[i*2]
        b = edges[i*2+1]

        arr[a].append(b)

    visited =set()
    stack =[]
    for i in range(1,n+1):
        if i not in visited:
            dfs(i,visited,stack)
    print(f'#{tc}',*stack[::-1])

'''
9 9
4 1 1 2 2 3 2 7 5 6 7 6 1 5 8 5 8 9
5 4
1 2 2 3 4 1 1 5
'''
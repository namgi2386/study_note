import sys
sys.stdin = open('z3.txt' , 'r')

n = int(input())  # 노드의 갯수
arr = [[] for _ in range(n+1)]
parent = [-1] * (n+1)  # 부모 기록

for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# BFS로 부모 찾기
q = [1]
parent[1] = -1  

while q:
    node = q.pop(0)
    for child in arr[node]:
        if not parent[child] : 
            parent[child] = node
            q.append(child)


for idx in range(2, n+1):
    print(parent[idx])
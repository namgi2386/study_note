def BFS(G, v):                      #
    # 준비과정
    visited = [0]*(n+1)             #visited = [ [0][0][0][0][0][0]...]
    queue = []                      #
    queue.append(v)                 # 시작지점 넣고 시작

    # 탐색과정
    while queue:                    #
        t = queue.pop(0)            # t = 방문할 노드
        if not visited[t]:          # 방문한적 없는 노드라면
            visited[t] = True       # 방문체크
            #visit(t)               #
            for i in G[t]:          # t와 연결된 노드 들에대하여
                if not visited[i]:  # 방문한적 없다면
                    queue.append(i) # 전부 큐에 넣기 (이따가 하나씩 뺄 예정)
n = 10
arr =[1,2]
v = 0
result = BFS(arr,v)


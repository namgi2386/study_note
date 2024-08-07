# 안간곳 w 상태 에서 방문하면 v 체크
# DFS(v)
#     시작점 v 방문 >> 스택에 시작점 등록
#     visited[v] <- true
#     while
#         if v의 인접 정점 중 방문 안한 정점 w가 있으면 :
#             push(v) # 방문한기록을 스택에 저장
#             v <- w w방문 # w로 이동
#             visited[w] <- true # 방문한 곳 기록하기
#         else:
#             if 스택이 비어있지 않으면: # 돌아갈곳이 있다면
#                 v <- pop(stack) #돌아가면서 기록삭제하기
#             else:
#                 break # 갈수있는곳이 없음. 끝남
# end DFS()

'''
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def DFS(s,n):               # s==시작점, n==정점갯수(1번부터인 정점의 마지막정점)
    visited = [0]*(n+1)     # 방문한 정점을 기록
    stack = []              # 스택생성
    print(s)
    visited[s] = 1          # 시작점 방문함을 표시
    v = s
    while True:
        for w in adjL[v]: # 현재위치 v와 연결된 점들 중 w
            if visited[w] == 0: # w의 visited값이 0이라면 (방문안한곳이라면)
                stack.append(v) # 스택에 저장해두기 (나중에 돌아오기위해)
                v = w           # w방문
                print(v)
                visited[w] = 1  # w 에 방문표시
                break           # v부터 다시탐색
        else:
            # 이전갈림길을 스택에서 꺼내서 이동할 예정인데
            if stack:
                v = stack.pop()
            else:
                break


T = int(input())
for tc in range(1,T+1):
    v , e = map(int,input().split())
    adjL = [[] for _ in range(v+1)]
    arr = list(map(int,input().split()))
    for i in range(e):
        v1 , v2 = arr[i*2] , arr[i*2+1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)
    #print(adjL)
    DFS(1,v)
'''
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


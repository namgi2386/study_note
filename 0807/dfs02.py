
# 그래프를 빠짐없이 한번씩 모두 방문 하는게 목표
# 그방법중 하나가 DFS

# 그래프를 표현하는 방법
# 인접리스트 , 인접행렬

# adj_m =[[] * n for _ in range(n)]
# adj_m[1][2] = 1
# 1번정점에서 2번정점으로 바로가는 간선이 존재한다 ( 0 이면 간선이 없음 )

# 4번에서 5번으로 가는 길이 있다, 무향 그래프라면 5반에서 4반으로 가는 길도 있음

adj_m = [[0,1,1,0,0,0,0],
         [1,0,0,1,1,0,0],
         [1,0,0,0,1,0,0],
         [0,1,0,0,0,1,0],
         [0,1,1,0,0,1,0],
         [0,0,0,1,1,0,1],
         [0,0,0,0,0,1,0],
         ]

def dfs_m(s,N):
    visited = [0]*(N+1) # 방문체크를 위한 체크표
    stack = [] # 돌아올 지점들은 stack에 기록된다
    visited[s] = 1 # 시작지점은 방문기록
    v = s # 현재 방문위치를 v라고 하자
    while True:
        # 현재 정점에서 갈 수 있는 길이 있는지 확인
        # 나머지 정점 번호를 i라고 할때 adf_m[v][i] == 1 를 확인
        # i 번째 정점을
        for i in range(N):
            if adj_m[v][i] == 1 and visited[i] == 0:
                stack.append(v)
                print(i)
                visited[i] = 1

                v = i

                break
        else:
            # 반복문 하는동안  break 안쳐맞음
            # 현재 정점 v에서 갈 수 있는 i 정점을 찾지 못함
            if stack:
                # 스택안에 원소가 있다 => 갈길이 남았다
                v = stack.pop()
            else:
                #스택안에 원소가 없다 => 갈 길이없다
                # 남은 정점이 없다. 탐색완료
                break
dfs_m(0,7)
"""
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
"""
V,E = map(int,input().split())
adj_m = [[0]*(V+1) for _ in range(V+1)]

for i in range(E):
    s,e = map(int, input().split())

    adj_m[s][e] = 1
    adj_m[e][s] = 1

dfs_m(1,V)

# 인접리스트
# 1번 정점에서 2번 정전ㅁ으로 가는 길이 있다.
# 1번 정점에서 3번 정점으로 가는 길도 있다.
# adj_l[1] = [2,3]
# 5번 정점에서 갈 수 있는길이 없다.
# adj_l[5] =[]
#adj_l = [[] for_ in range(V) ]
def dfs_l(s,V):
    # 방문배열
    visited = [0]*(V+1)
    stack = []
    visited[s] = 1
    v = s
    print(v)

    while True:
        for i in adj_l[v]:
            if not visited[i]:
                stack.append(v)

                print(i)

                visited[i] = 1
                v = i
                break
        else:
            if stack:
                v = stack.pop()

            else:
                break

V,E = map(int,input().split())
adj_l = [[] for _ in range(V+1)]

for i in range(E):
    s,e = map(int, input().split())

    adj_l[s].append(e)
    adj_l[e].append(s)

adj_l(1,V)











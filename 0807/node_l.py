import sys
sys.stdin = open('z1.txt','r')

def dfs_l(s,V):
    # 방문배열
    visited = [0]*(V+1)
    stack = []
    visited[s] = 1
    v = s
    all_way =[]
    while True:
        # print(stack , v)
        for i in adj_l[v]:
            if not visited[i]:
                stack.append(v)
                # print(i)
                visited[i] = 1
                v = i
                break
        else:
            if stack:
                way = stack.copy()
                way.append(v)
                all_way.append(way)
                v = stack.pop()
            else:
                return all_way



T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    adj_l = [[] for _ in range(V+1)]
    total_way = []
    for i in range(E):
        s,e = map(int, input().split())
        adj_l[s].append(e)

    for i in range(1,V+1):
        total_way.extend(dfs_l(i,V))
    my_s, my_e = list(map(int, input().split()))
    result = 0
    for i in range(len(total_way)):
        if total_way[i][0] == my_s and total_way[i][-1] == my_e:
            result = 1

    print(total_way)
    print(f'#{tc} {result}')

import sys
sys.stdin = open('z1.txt','r')
def dfs_m(s,N):
    visited = [0]*(N+1)
    stack = []
    visited[s] = 1
    v = s
    all_way =[]
    while True:
        for i in range(N):
            if adj_m[v][i] == 1 and visited[i] == 0:
                stack.append(v)
                #print(i)
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
                break

T = int(input())
for i in range(1,T+1):
    V,E = map(int,input().split())
    adj_m = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        s,e = map(int, input().split())

        adj_m[s][e] = 1
        adj_m[e][s] = 1
    my_s , my_e = map(int, input().split())

    dfs_m(1,V)
# def f(s_node,e_node):

# for i in range(1,n+1):
#     if not arr[i] :
#         for j in range(i,n+1):
#             if not arr[j]:
#                 f(i,j)

# def f(node , weight):
#     if not arr[node]:
#         pass # 단말노드 도착
    
#     for i in arr[node]:
#         weight +=  i[1]
#         f(i[0] , weight)

def f():
    idx = s.pop()
    solve_arr[p[idx]][0] += arr[idx][1]
    solve_arr[p[idx]][1] = max( arr[idx][1] , solve_arr[p[idx]][1] )
        



n= int(input())
arr = [[] for _ in range(n+1) ]
p = [0]*(n+1) 
for _ in range(n-1):
    a,b,w = map(int,input().split())
    arr[a].append((b,w))
    p[b] = a

s =[]
solve_arr =[[0]*2 for _ in range(n+1) ]
for i in range(1,n+1):
    if not arr[i]:
        s.append(i)
        # solve_arr 에 단말노드 정보 담아둬야댐
f()
print(solve_arr)




from collections import deque

def we(stack):
    result_arr = [1]*(n+1)
    while stack:
        idx = stack.popleft()
        for inner_idx in arr[idx]:
            num[inner_idx] -= 1
            result_arr[inner_idx] = result_arr[idx] +1
            if num[inner_idx] == 0:
                stack.append(inner_idx)

    print(*result_arr[1:])


n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
num = [0]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    num[b] += 1

start_s = deque()
for i in range(n):
    if num[i] == 0:
        start_s.append(i)
we(start_s)
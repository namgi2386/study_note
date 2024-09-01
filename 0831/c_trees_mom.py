import sys
sys.stdin = open('z3.txt' , 'r')

n = int(input())            # 노드의 갯수
left =[0]*(n+1)
right =[0]*(n+1)
up =[0]*(n+1)


parent =[-1]*(n+1)             # 노드갯수 +1개
parent[1]=0

for i in range(n-1):

    a,b = map(int, input().split())

    if left[a] :
        if up[a]
        right[a] = b
    else:
        left[a] = b

    if left[b] :
        right[b] = a
    else:
        left[b] = a


    if parent[a]== -1 :  # 입력값 이상하면 위치변경
        a,b = b,a
    parent[b] = a           # 기록

print(left)
print(right)
# for idx in range(2,n+1):
#     print(parent[idx])

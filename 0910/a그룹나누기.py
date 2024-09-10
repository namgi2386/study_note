import sys
sys.stdin = open('z1.txt','r')

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parents[root_x] = root_y

for tc in range(1,int(input())+1):
    n,m = map(int,input().split()) # 5 2
    parents = [i for i in range(n+1)]

    arr =list(map(int,input().split()))

    for i in range(len(arr)//2):
        a = arr[2*i]
        b = arr[2*i+1]
        union(a,b) # union(1,2) 이후 union(3,4) 실행됨


    #print(parents) # 부모가 저장되어있는 상태
    for i in range(1,n+1):
        find(i)
    #print(parents) # 대표가 저장되어있는 상태


    s=set() # 중복제거하기
    for i in range(n+1):
        s.add(parents[i])

    print(f'#{tc} {len(s)-1}')


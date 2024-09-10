import sys
sys.stdin = open('z1.txt','r')

def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        p[root_x] = root_y

for tc in range(1,int(input())+1):
    n,m = map(int,input().split()) # 5 2
    p = [i for i in range(n+1)]
    p2 = list(range(n+1))

    arr =list(map(int,input().split()))

    for i in range(len(arr)//2):
        a = arr[2*i]
        b = arr[2*i+1]
        union(a,b) # union(1,2) 이후 union(3,4) 실행됨


    #print(p) # 부모가 저장되어있는 상태
    for i in range(1,n+1):
        find(i)
    #print(p) # 대표가 저장되어있는 상태


    s=set() # 중복제거하기
    for i in range(n+1):
        s.add(p[i])

    print(f'#{tc} {len(s)-1}')

###################################남희코드
    # 각 학생의 대표를 찾고 집합의 수를 세기 위한 준비
    result = [find(i) for i in range(1, n + 1)]

    # 대표자 집합의 수를 계산하여 출력
    print(f'#{tc} {len(set(result))}')
#########################################

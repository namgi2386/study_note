import sys
sys.stdin = open('z4.txt' , 'r')
def find_set(x):
    if p[x] == x:
        return x
    p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    x = find_set(x)
    y = find_set(y)

    if x!=y:
        p[x] = y

for tc in range(1,int(input())+1):
    n = int(input())
    x_arr = list(map(int,input().split()))
    y_arr = list(map(int,input().split()))
    cost = float(input())
    rocation_arr = [0]*n
    for i in range(n):
        rocation_arr[i] = (x_arr[i], y_arr[i])
    
    weight_arr =[]

    for i in range(n-1):
        for j in range(i+1,n):
            ax,ay = rocation_arr[i]
            bx,by = rocation_arr[j]
            w = abs(ax-bx)**2 + abs(ay-by)**2
            weight_arr.append((i,j,w))
    
    weight_arr.sort(key=lambda x : x[2])   # 가중치기준 정렬
    p = list(range(n))

    cnt = 0 # 이제까지 간선 몇개 선택했는지 기록함
    total = 0
    for a,b,w in weight_arr:
        if find_set(a) != find_set(b):
            cnt += 1
            union(a,b)
            total += cost*w
            if cnt == n:
                break
    print(f'#{tc} {int(round(total))}')



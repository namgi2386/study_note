
def find_set(x):
    if p[x] == x:
        return x
    p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    x = find_set(x)
    y = find_set(y)

    if x==y:
        return
    if x<y:
        p[y] = x
    else:
        p[x] = y



n,m = map(int,input().split())
arr = []
for _ in range(m):
    a,b,w = map(int,input().split())
    arr.append((a,b,w))
arr.sort(key=lambda x : x[2])   # 가중치기준 정렬
p = list(range(n))              # 부모를 기록하기 위한 리스트 생성




cnt = 0 # 이제까지 간선 몇개 선택했는지 기록함
total = 0
for a,b,w in arr:
    print(a,b,w)
    if find_set(a) != find_set(b):
        cnt += 1
        union(a,b)
        total += w
        if cnt == n:
            break
print(f'최소비용 = {total}')
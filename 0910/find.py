# n개 원소가 있는 집합
n=10
p = [ i for  i in range(n)] # 이게 make_set 하기
print(p) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 연산 최적화위한 rank배열
rank = [1]*n
print(rank) # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# x가 속한 집합의 대표를 찾는 연산
def find(x):
    if p[x] == x : # 나의부모가 나자신
        return x
    if p[x] != x : # 부모 존재
        p[x] = find(p[x]) # 부모의부모를 찾아와서 부모로 설정하기 (경로압축)

# def find(x):
#     if p[x] != x :
#         p[x] = find(p[x])
#     return x

def union(x,y):
    # x와 y는 대표가 아닌 구성원일 수도 있다.
    # 각자의 대표끼리의 union을 해줘야해
    rootX = find(x)
    rootY = find(y)

    if rootX == rootY: # 이미 대표가 같내?
        return

    # rank 값에 따라 큰거에 작은거 붙이기
    if rank[rootX] > rank[rootY]:
        p[rootY] = rootX
    elif rank[rootX] < rank[rootY]:
        p[rootX] = rootY
    else:
        p[rootY] = rootX
        rank[rootX] += 1 # 랭크같으면 랭크 1 증가
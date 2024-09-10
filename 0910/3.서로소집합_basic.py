def make_set(n):
    p = [i for i in range(n)]  # 각 원소의 부모를 자신으로 초기화
    return p


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return find(parents[x])


def union(x, y):
    root_x = find(x) # 각자의 대표자 찾아오기
    root_y = find(y)

    if root_x == root_y:  # 이미 같은 집합이면 끝
        return

    # 다른 집합이라면 더 작은 루트노트에 합친다.
    if root_x < root_y:
        parents[y] = root_x # y가 바라보는 부모는 x의 대표입니다.
    else:
        parents[x] = root_y


# 예제 사용법
n = 3  # 원소의 개수
parents = make_set(n)

union(1,2)
# union(4,5)
# union(4,6)
# union(7,4)
print(parents)
for i in range(n):
    find(i)
print(parents)

s=set()
for i in range(n):
    s.add(parents[i])
print(s)
print(len(s)-1)

# print('find_set(6) = ', find(6))
#
# target_x = 2
# target_y = 3
#
# # 원소 1과 원소 2가 같은 집합에 속해 있는지 확인
# if find(target_x) == find(target_y):
#     print(f"원소 {target_x}과 원소 {target_y}는 같은 집합에 속해 있습니다.")
# else:
#     print(f"원소 {target_x}과 원소 {target_y}는 다른 집합에 속해 있습니다.")

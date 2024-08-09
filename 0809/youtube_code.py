def backtrack(a, k, n):
    # a:주어진배열 k:결정할원소 n:원소개수
    c = [0] * MAXCANDIDATES
    # c:후보추천 및 저장

    if k == n:  # 트리의 밑바닥에 도착했을때
        process_solution(a, k)

    else:
        ncandidates = construct_candidates(a, k, n, c)
        # ncan..:2개 , c: [0or1]
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)
            # 재귀호출
def construct_candidates(a, k, n, c):
    c[0] = True
    c[1] = False
    return 2
def process_solution(a, k):
    for i in range(k):
        if a[i]:
            print(num[i], end='')
    print()
MAXCANDIDATES = 2
NMAX = 4
arr = [0] * NMAX
num = [1, 2, 3, 4]
# backtrack(arr, 0, NMAX)

# --------------------------------------------------------

# for i1 in range(1,4):
#     for i2 in range(1, 4):
#         if i2 != i1:
#             for i3 in range(1, 4):
#                 if i3 != i1 and i3 != i2:
#                     print(i1,i2,i3)

# --------------------------------------------------------

def backtrack(a, k, n):
    # a:주어진배열 k:결정할원소 n:원소개수
    c = [0] * MAXCANDIDATES # 후보 저장할 배열
    # c:후보추천 및 저장

    if k == n:  # 트리의 밑바닥에 도착했을때
        for i in range(0,k):
            print(a[i],end=" ")
        print()
    else:
        ncandidates = construct_candidates(a, k, n, c)
        # ncandidates:3,2,1,...변경됨
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)
def construct_candidates(a, k, n, c):
    in_perm = [False]*(NMAX+1) # 여기에 사용된적 있는지 없는지 체크함

    for i in range(k):
        in_perm[a[i]] = True
        # a[0] ~~ a[k-1] 중 사용한 적 없는 후보를 추천할 예정
        # a[k]에 들어갈 후보를 c에 추천할 예정

    ncandidates = 0
    for i in range(1, NMAX +1):
        if in_perm[i] == False: # 사용된 적 없는 애들을
            c[ncandidates] = i  # c에 넣어줌
            ncandidates += 1
    return ncandidates # 최종적으로 실제 추천할 갯수
MAXCANDIDATES = 3
NMAX = 3
arr = [0] * NMAX
# backtrack(arr, 0, NMAX)

# --------------------------------------------------------

# a [ ][ ][ ] 1,2,3으로 순열 만들건데
#    ^ 이자리에 넣을 수 있는 후보군이 c 에 저장되어있다
# c [1,2,3] 3개 아무거나 넣을수 있는상태
#
# a [2][ ][ ] 2를 우선 넣은 상태
#       ^ 이제 이자리에 넣을 후보군 c를 확인
# c [1,3] 둘중에 선택가능
# a [2][1][ ] 1넣음
# c [3]
# a [2][1][3]
# c [] 이제 넣을수있는게 없음

# --------------------------------------------------------

def f(i,K): # bit[i]를 결정하는 함수
    if i == K: # 모든원소에 대해 결정하면
        for j in range(K):
            if bit[j]: # bit[j]가 0이아니면
                print(a[j], end =" ")
        print()
    else:
        bit[i] = 1
        f(i+1, K)
        bit[i] = 0
        f(i+1 , K)

N =3
a =[1,2,3]  # 주어진 원소의 집합
bit = [0]*N # 원소의 포함여부를 표시하는 배열
# f(0, N) # N개의 원소에 대해 부분집합을 만드는 합수 실행
# --------------------------------------------------------
# bit[i]를 결정하는 함수
def f(i, K):
    if i == K: # 모든원소에 대해 결정하면
        s = 0
        for j in range(K):
            if bit[j]: # bit[j]가 0이아니면
                # print(a[j], end =" ")
                s += a[j]
        print(' : ', s)
    else:
        # bit[i] = 1
        # f(i+1, K)
        # bit[i] = 0
        # f(i+1 , K)
        for j in [1,0]:
            bit[i] = j
            f(i+1,K)

N = 3
a =[1,2,3]  # 주어진 원소의 집합
bit = [0]*N # 원소의 포함여부를 표시하는 배열
#f(0, N) # N개의 원소에 대해 부분집합을 만드는 합수 실행

# --------------------------------------------------------

def f2(i , N , s , t):
    if s == t:
        pass
    elif i == N:
        pass
    elif s> t:
        pass
    else:
        subset[i] = 1
        f2(i+1 , N, s+A[i], t) # 이전원소합에 i 원소 포함
        subset[i] = 0
        f2(i+1,N,s,t)  # 이전원소합에 i 원소 미포함
# 추가 고려사항
# 이전원소합 s  > t 이면 중단
# 이전원소합 s + 남은구간합 RS  < t 일때도 중단

# --------------------------------------------------------
# 부분집합(A)의 합이 (key)인 부분집합의 갯수(cnt)
def f(i,k,s,t):
    global cnt
    global fcnt
    fcnt += 1
    if i == k:
        if s==t:
            cnt += 1
        return
    else:
        bit[i] = 1
        f(i+1 , k,s+A[i] , t)
        bit[i] = 0
        f(i+1 , k,s , t)


A = [1,2,3,4,5,6,7,8,9,10]
N = 10
key = 10
cnt = 0         # 합이 key와 같은 부분집합의 수
fcnt = 0        # 실행횟수
bit = [0]*N
f(0,N,0,key)
print(cnt , fcnt)
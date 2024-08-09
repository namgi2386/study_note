> 어제 내용 이어서
# 🌏부분집합 + 분할정복🌏

___
## 🗽부분집합🗽
#### 🏠이전에 2진수 비트를 이용한 방법이 있었다.  
```python
arr = [1,2,3]  ### 참고만 하고 넘어가기
result = []
for i in range(1<<len(arr)): 
  subset = []
  for j in range(len(arr)): 
    if i & (1<<j): 
      subset.append(arr[j]) 
  result.append(subset)
print(result)
```
#### 🏫백트래킹을 이용한 부분집합 만들기  
```python
# 이거 만들어보자
1234, 123, 124, 12, 134, 13, 14, 
1, 234, 23, 24, 2, 34, 3
```
```python
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
backtrack(arr, 0, NMAX)
```
## 🗼순열🗼
> A형시험을 위해 순열 조합 부분집합 개념 숙지   
> 알고리즘의 기본은 모든 경우의수를 체크해본 뒤  
> 쓸모없는 경우를 제거하는 순서로 진행되는데  
> 모든 경우의수를 체크하는 방법이  
> 순열 조합 부분집합 이다!  
#### 🏣집합 {1,2,3}에서 모든 순열을 생성해보기
```python
for i1 in range(1,4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1,i2,i3)
```
```python
# 결과
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```
> 앞선 부분집합과는 달리 각 노드에서의 
> 후보군의 갯수가 일정한 것이 아니다
#### 🏭백트래킹으로 {1,2,3} 순열만들기
`개념`🧱
```python
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
```
`코드`🧱
```python
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
backtrack(arr, 0, NMAX)
```
## 🕋[참고]🕋 부분집합의 합 (가지치기)
#### 🏩우선 원소3개 부분집합 만들기
```python
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
f(0, N) # N개의 원소에 대해 부분집합을 만드는 합수 실행
```
#### 🏦부분집합 합 만들기
```python
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
f(0, N) # N개의 원소에 대해 부분집합을 만드는 합수 실행
```
#### 🏬추추가
```python
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
```
#### 💒부분집합(A)의 합이 (key)인 부분집합의 갯수(cnt)
```python
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
```

## 🌉강사님 추가설명🌉
<details>
<summary>
⛲열어보기 : 부분집합만들기
</summary>

```python
lst = [1,2,3,4,5]
li = []
N =5
S = 10
#print(lst)

# 0번째 원소를 고를까말까
# 1번쨰 원소를 고를까말까 ...


# selected : 내가 고른 원소 체크하기
# 만약 selected[x] == 1 : x번째 원소를 부분집합에 포함시킨상태
# n : 원소의 전체 개수
# s : 지금까지 구한 부분집합의 합

# idx번째 원소를 고를지 말지 선택하는 함수
def make_subset(idx , selected , n , s):
    global li

    # 가지치기 - 답이 될 가능성 없으면 진행하지 않기위해 사용
    if s > S:
        return

    # 종료조건
    if idx == n : # lst에는 인덱스가 n-1까지라서 idx == n라는건, 밖으로 나갔다는 뜻
        subset = []
        for i in range(n):
            if selected[i]:
                subset.append(lst[i])
        print(subset , end=" ")
        li.append(subset)
        return

    # 재귀호출 ( 여기서 부분집합을 만들 selected 만듬 )
        # idx 번째 원소에 대하여
        # 부분집합에 idx번째 원소를 포함할지 말지 정해
    selected[idx] = 1 # 넣었다면
    make_subset(idx+1, selected , n , s+ lst[idx]) # 다음원소 확인하러 가기

    selected[idx] = 0 # 넣지 않았다면 ( 넣었었으니까 다시빼기 )
    make_subset(idx + 1, selected, n , s)  # 다음원소 확인하러 가기

    # selected == [1,1,1,1,1] : 전부고른상태

make_subset(0, [0]*N , N , 0) # idx 0번부터 실행 , 빈칸N개짜리 만들어두고 시작
print()
print(len(li))
```


</details>

<details>
<summary>
⛲열어보기 : 순열만들기
</summary>

```python
lst = [1,2,3,4,5]
N = 5

# idx : 현재 순열의 i번째 자리에 올 원소를 선택하고 있다.
# selected : 순열 만들때 이전에 사용했던 원소 체크하기
# result : 지금까지 만든 순열
# n 순열 길이
def make_perm(idx , selected , result , n):

    # 종료조건
    if idx == n:
        print(result)
        return


    # 재귀호출

    # 현재순열의 idx 번째 자리에 놓을 원소선택
    # 이전에 고른적이 없는 원소를 자리에 놓아야함
    # 내가 고를 수 있는 원소는 lst 안에 있음
    # lst 인덱스 범위는 0~n-1
    for i in range(n):
        # i번째 원소를 이전에 고른 적이 없다면 순열의 idx 번째 자리에 i번 원소를 놓는다.
        if selected[i] == 0: # i번째 원소는 사용한적 없음
            # i번째 원소를 골랐다고 기록하고 넘어가야함
            selected[i] = 1
            result.append(lst[i])
            # idx+1 번째 자리에 넣을 원소 정하러가기
            make_perm(idx+1 , selected , result , n )

            # i번째 원소 원상복귀
            selected[i] = 0
            result.pop()
make_perm(0,[0]*N , [] , N)
```


</details>

<details>
<summary>
⛲열어보기 : idx번째 자리에 있는 원소를 다른 우너소와 바꿔서 순열 만들어보기
</summary>

```python
lst = [1,2,3,4,5]


# idx : idx번째 자리에 있는 원소를 다른 우너소와 바꿔서 순열 만들어보기
# n 순열의 길이
def make_perm(idx , n):
    # 종료조건
    if idx == n:
        print(lst)
        return

    # 재귀조건
    # idx 번째 원소와 다른위치 ( j )에 있는 원소 자리바꿔보기
    # idx == j : 자리를 바꾸지 않겠다.
    # 자리를 바꿀 j를 선택해보자
    for j in range(idx , n ):
        # idx 번째 원소와 j번째 원소의 자리 교환
        lst[idx] , lst[j] = lst[j] ,  lst[idx]

        # idx + 1 번째 자리 바꾸러 가기
        make_perm(idx+1,n)

        # 자리 원래대로 되돌려 놓기
        lst[idx] , lst[j] = lst[j] ,  lst[idx]

make_perm(0,5)
```


</details>
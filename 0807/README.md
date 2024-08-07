> 어제 내용 이어서 ~

## memoization🥗

> + 피보나치 수열의 call tree 
>  ```python
>  def pivonachi():
>   f(n) = f(n-1) + f(n-2) <<< 이런식으로해버리면 
>   f(7) = f(6) +f(5)
>   f(7) = f(5)+f(4) + [ f(4) +f(3) ]
>   f(7) = [ f(4) +f(3) ] +[f(3)+f(2)] + [ [f(3)+f(2)] +[f(2)+f(1)] ]
>   f(7) = .......  너무 많은 중복되는 계산과정
>  ```
> + 이떄의 복잡도는 `2^n` 존나복잡함

### 기존의 재귀함수🥦
```python
def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(35))
```

### 개선된 momoization 피보나치수열 재귀함수🥬
```python
def fibo1(n):
    global memo
    if n >= 2 and memo[n] == 0: 
        # fibo(n)이 계산된적 없다면 실행됨.  
        # >> 즉 이미 계산된 적 있다면 실행하지 않고 return으로감
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n] # 이전에 계산했던 값을 가져옴

n= 7
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
fibo1(n)
print(memo)
```
## 동적할당 DP🥑
> DP사용하면 짧고 멋진 코드 가능
> 
> 최적화를 위한 알고리즘
> 
> ### B형준비하는거 아니면 필요없음

### 피보나치 DP 적용 알고리즘🥒
```python
def fibo2(n):
    f = [0]*(n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2,n+1):
        f[i] = f[i-1] + f[n-2]
    return f[n]
```
### DP 구현 방식🌽
> + recursive : `fib1()`
> + iterative : `fib2()`

## DFS 깊이우선탐색🥕
> 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함
> + **깊이 우선 탐색 DFS**
> + 너비 우선 탐색 BFS (나중에)

> 지나온 길의 갈림길들을 기억해둔 상태로 하나의 길로만 이어나가다가 막다른길에 도달하게 되면,  
> 가장 마지막에 마주쳤던 갈림길로 돌아간 뒤 선택하지 않았던 길로 여행 떠남.  
> 이 과정반복하여 모든 길을 탐색

> 마치, 마주쳤던 갈림길을 스택형식으로 저장해 놓은 것과 같음. 
### DFS 예시🥔
#### 이런느낌?
```python
안간곳 w 상태 에서 방문하면 v 체크
DFS(v)
    시작점 v 방문 >> 스택에 시작점 등록
    visited[v] <- true
    while
        if v의 인접 정점 중 방문 안한 정점 w가 있으면 :
            push(v) # 방문한기록을 스택에 저장
            v <- w w방문 # w로 이동
            visited[w] <- true # 방문한 곳 기록하기
        else:
            if 스택이 비어있지 않으면: # 돌아갈곳이 있다면
                v <- pop(stack) #돌아가면서 기록삭제하기
            else:
                break # 갈수있는곳이 없음. 끝남
end DFS()
```
### DFS 실습🧄
```python
'''
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def DFS(s,n):               # s==시작점, n==정점갯수(1번부터인 정점의 마지막정점)
    visited = [0]*(n+1)     # 방문한 정점을 기록
    stack = []              # 스택생성
    print(s)
    visited[s] = 1          # 시작점 방문함을 표시
    v = s
    while True:
        for w in adjL[v]: # 현재위치 v와 연결된 점들 중 w
            if visited[w] == 0: # w의 visited값이 0이라면 (방문안한곳이라면)
                stack.append(v) # 스택에 저장해두기 (나중에 돌아오기위해)
                v = w           # w방문
                print(v)
                visited[w] = 1  # w 에 방문표시
                break           # v부터 다시탐색
        else:
            # 이전갈림길을 스택에서 꺼내서 이동할 예정인데
            if stack:
                v =stack.pop()
            else:
                break


T = int(input())
for tc in range(1,T+1):
    v , e = map(int,input().split())
    adjL = [[] for _ in range(v+1)]
    arr = list(map(int,input().split()))
    for i in range(e):
        v1 , v2 = arr[i*2] , arr[i*2+1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)
    #print(adjL)
    DFS(1,v)
'''
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
```








<details>
<summary>
  강사님 추가설명
</summary>

```py

# 그래프를 빠짐없이 한번씩 모두 방문 하는게 목표
# 그방법중 하나가 DFS

# 그래프를 표현하는 방법
# 인접리스트 , 인접행렬

# adj_m =[[] * n for _ in range(n)]
# adj_m[1][2] = 1
# 1번정점에서 2번정점으로 바로가는 간선이 존재한다 ( 0 이면 간선이 없음 )

# 4번에서 5번으로 가는 길이 있다, 무향 그래프라면 5반에서 4반으로 가는 길도 있음

adj_m = [[0,1,1,0,0,0,0],
         [1,0,0,1,1,0,0],
         [1,0,0,0,1,0,0],
         [0,1,0,0,0,1,0],
         [0,1,1,0,0,1,0],
         [0,0,0,1,1,0,1],
         [0,0,0,0,0,1,0],
         ]

def dfs_m(s,N):
    visited = [0]*(N+1) # 방문체크를 위한 체크표
    stack = [] # 돌아올 지점들은 stack에 기록된다
    visited[s] = 1 # 시작지점은 방문기록
    v = s # 현재 방문위치를 v라고 하자
    while True:
        # 현재 정점에서 갈 수 있는 길이 있는지 확인
        # 나머지 정점 번호를 i라고 할때 adf_m[v][i] == 1 를 확인
        # i 번째 정점을
        for i in range(N):
            if adj_m[v][i] == 1 and visited[i] == 0:
                stack.append(v)
                print(i)
                visited[i] = 1

                v = i

                break
        else:
            # 반복문 하는동안  break 안쳐맞음
            # 현재 정점 v에서 갈 수 있는 i 정점을 찾지 못함
            if stack:
                # 스택안에 원소가 있다 => 갈길이 남았다
                v = stack.pop()
            else:
                #스택안에 원소가 없다 => 갈 길이없다
                # 남은 정점이 없다. 탐색완료
                break
dfs_m(0,7)
"""
7 6
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
"""
V,E = map(int,input().split())
adj_m = [[0]*(V+1) for _ in range(V+1)]

for i in range(E):
    s,e = map(int, input().split())

    adj_m[s][e] = 1
    adj_m[e][s] = 1

dfs_m(1,V)

# 인접리스트
# 1번 정점에서 2번 정전ㅁ으로 가는 길이 있다.
# 1번 정점에서 3번 정점으로 가는 길도 있다.
# adj_l[1] = [2,3]
# 5번 정점에서 갈 수 있는길이 없다.
# adj_l[5] =[]
#adj_l = [[] for_ in range(V) ]
def dfs_l(s,V):
    # 방문배열
    visited = [0]*(V+1)
    stack = []
    visited[s] = 1
    v = s
    print(v)

    while True:
        for i in adj_l[v]:
            if not visited[i]:
                stack.append(v)

                print(i)

                visited[i] = 1
                v = i
                break
        else:
            if stack:
                v = stack.pop()

            else:
                break

V,E = map(int,input().split())
adj_l = [[] for _ in range(V+1)]

for i in range(E):
    s,e = map(int, input().split())

    adj_l[s].append(e)
    adj_l[e].append(s)

adj_l(1,V)
```
</details>


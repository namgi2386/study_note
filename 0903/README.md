# 📚완전 검색

## 🔖목차
[반복과 재귀](#반복과-재귀)  
[순열](#순열)  
[완전 탐색](#완전-탐색)  
[부분 집합(~0903)](#부분-집합-0903)  
[조합](#조합)  
[탐욕 알고리즘](#탐욕-알고리즘)  

---

## 📕반복과 재귀
#### 📜지역변수와 전역변수
> 변수와 리스트의 차이 이해하기
+ 재귀가 언제 끝날지 ==> a == b 일때, 혹은 인덱스가 n이 됐을때   
+ 재귀를 하면서 뭐가 바뀌길 워하는가? == 몇번째 원소에 접근하는지!  

```py
def h(x,y):
    print(f'2 x  {x}') # 10
    print(f'2   y  {y}') # 30
    x[0] += 1
    y += 2
    print(f'3 x  {x}') # 11
    print(f'3   y  {y}') # 32

x = [10]
y = 30
print(f'1 x  {x}') # 10
print(f'1   y  {y}') # 30
h(x,y)
print(f'4 x  {x}') # 11 (수정됨)
print(f'4   y {y}') # 30 (수정안됨)
```
```py
def b(x) # x = 14
    print(x)        # 14 출력 (2)

def a(x) # x = 8
    print(x)    # 8 출력 (1)
    x += 1 # x = 9
    b(x+5) 
    print(x)            # 9 출력 (3)

x = 3
a(x+5)
print(x)                    # 3 출력 (4)

```
#### 📜무한 재귀 종료하기
> 종료조건 호출전후 , 전달할 인자 check!
```py
def f(x):
    if x == 6:          # 종료조건
        return
    print(x, end=" ")   # 호출전
    f(x+1)              # 인자 전달
    print(x,end=" ")    # 종료후
f(1) # 1 2 3 4 5 5 4 3 2 1
```

## 📗순열
#### 📜중복순열
> n개 중 r개를 중복허용 뽑기
```py
s = []
def f_5():
    if len(s) == 3: 
        print(*s)
        return
    
    for i in range(1,7):
        s.append(i)
        f_5()
        s.pop()
f_5()
print('-*-'*10)

s = []
def f_6(x): # 매 level 마다 요소 하나씩 추가할 예정
    if x ==3: # 종료조건 3개의 요소가 추가되었을때 (level == 3 일때)
        print(*s) # 출력 후 리턴
        return
    for i in range(1,7): # 각 level에서 넣을 값은 1~6
        s.append(i) # 요소를 하나 넣음
        f_6(x+1) # 다음 level(=x+1)로 이동
        s.pop() # 돌아왔을때 pop하기
f_6(0)
print('-*-'*10)
```

#### 📜순열 (중복x)
> n개 중 r개를 중복없이 뽑기
```py
s = []
visited = [0]*7
def f_7():
    if len(s) == 3: 
        print(*s)
        return
    
    # 방문 한적없다면 실행
    # 혹은, 방문 했었다면 continue
    for i in range(1,7):
        if not visited[i]:
            visited[i] = 1
            s.append(i)
            f_7()
            s.pop()
            visited[i] = 0
f_7()
print('-*-'*10)
```

## 📙완전 탐색
> 서로 영향이 없는 독립적인 문제에 대해  
> 규칙이 없다면, 완전탐색  
```py
path = []

# 주사위 몇개던짐?
# 합이 몇임?
def recur(level,total):

    if total > 10: # 가지치기
        return

    if level==3: # 종료조건
        if total <= 10 :
            print(f'{path} = {total}')
        return

    for i in range(1,7): 
        path.append(i)
        recur(level+1,total+i)
        path.pop()

recur(0,0) # 실행
```


## 📒부분 집합 (~0903)

#### 📜 완전탐색으로 부분집합 구하기
```py
arr = {'o','x'}
path = []
name = ['min' , 'co' , 'tim']

def print_name():
    print('{' , end ="")
    for i in range(3):
        if path[i] == 'o':
            print(name[i] , end=" ")
    print('}')

def run(lev):
    if lev == 3:
        print_name()
        return
    
    for i in range(2):
        path.append(arr[i])
        run(lev + 1)
        path.pop()

run(0)
```

#### 📜 binary로 부분집합 만들기
```py
mem = ['a','b','c','d','e']

def bib(t):
    cnt =0
    checj_arr =[]
    for i in range(n):
        if t & (1<<i):
            cnt += 1
            checj_arr.append(mem[i])
    total_arr.append(checj_arr[:])
    return cnt

n =5
result = 0
total_arr = []
for rr in range(1<<n):
    
    if bib(rr) >= 2:
        result += 1
        print(total_arr)
    print(result)
```

## 📔조합

```py
def dice(t , p):
    if len(s)==3:
        print(s)
        return

    for i in range(p,7):
        s.append(i)
        dice(t+1 , i)
        s.pop()

s=[]
dice(0,1)
```

#### 📜 주사위만들기
```py
#idx 0 1 2 3 4
A = [1,2,3,4,5]

N=5
# idx : 부분집합에 넣을지 맣지 결정하는 원소의 위치

# 다음 재귀호출에서 이전 단계에서 골랐던 원소들을 알려줄 배열
# selected , visited , s 등
def subset(idx , selected):
    # 1. 종료조건
    if idx == N:
        print(selected)
        return
    # 2. 재귀호출
    # 각 단계에서 분기 수 만큼 재귀 호출
    # 부분집합에서의 분기는 idx번째 원소의 선택여부에따라 2가지로 나뉨

    # idx번째 원소 고른 이후 idx+1번째 원소를 선택하러 가기
    
    # selected.append(A[idx])
    # subset(idx+1,selected)
    
    subset(idx+1,selected + [A[idx]]) #이걸로한다면 되돌리지 않아도됨

    # 분기가 나눠질때 이전 선택에서 했던 일을 되돌려놔야함

    # idx번째 원소를 고르지 않고 idx +1번째 원소 선택하러가기
    
    subset(idx+1,selected)

subset(0,[])
```



## 📘탐욕 알고리즘
> 탐욕알고리즘에도 유형이 있다. 그유형일때만 이거해야됨.
+ 각단계의 최적해 찾기
+ 단계의 결과들을 합하는 방법 찾기
+ 각 단계의 합이 전체의 합이라는것을 증명해야함



#### 메모
+ 디스코드 대기방
  + 각자 따로 코딩
  + 시간정해서 디스코드 화면공유 
+ 문제선정 매일 풀이 올리기 
+ 월 수목 (오늘의 추가문제) 3명선정 모두풀어서 제출 후 일요일 발표
+ 풀었던 문제 중 골라서 설명하기
  + 매일 문제 정리 
  + 어제내용 복습리뷰
+ 모의시험 진행
  + 시간제한 문제풀이
+ cs 해야되나
+ 단톡방 no

#### 링크첨부
<a href="https://swanky-warbler-d07.notion.site/1-30-520ccd12a4f940b498e67d13b018a85f">세황</a>
<hr>
<a href=""></a>
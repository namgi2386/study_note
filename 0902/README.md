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

## 📔조합

## 📘탐욕 알고리즘
# 🎪큐 Queue🎪 

### 🦆큐🦆 
> first in first out

<img src=https://velog.velcdn.com/images%2Fsuitepotato%2Fpost%2F482139b5-de8a-41bf-af3b-1e5ae1519773%2Fqueue_concept_01.PNG>

['image link'](https://velog.io/@suitepotato/00004)

### 🦢큐 연산과정 + charmgo sahang🦢
+ `creatQueue()` 공백 큐 생성 # front = rear = -1
+ `enQueue()` 원소 A 삽입     # front = -1 , rear = 0
+ `enQueue()` 원소 B 삽입     # front = -1 , rear = 1
+ `deQueue()` 원소 반환/삭제  # front = 0 , rear = 1  

> `front` : 가장 최근에 반환된 자리 (즉, front엔 빈칸)  
> `삽입` : 자리가 있어야 삽입가능  
> `isEmpty` : front =?= rear  
> `isFull` : rear =?= n-1  
> `Qpeek` : 첫번째 원소 반환

### 🦅간단하게 큐 구현🦅
```py
      # 큐 생성
n = 10
q = [0]*n
front = -1
rear = -1

      # 큐에 요소 삽입
rear += 1
q[rear] = 'a'

rear += 1
q[rear] = 'b'

rear += 1
q[rear] = 'c'

      # 큐의 요소 반환
front += 1
print(q[front])

front += 1
print(q[front])

front += 1
print(q[front])

      # append,pop으로 간단하게 해보기
q2 = []
q2.append(10)
q2.append(20)
print(q2.pop(0))
print(q2.pop(0))
```

### 🦜원형큐🦜
> 선형큐에선 front rear이 뒤로 이동하며 앞쪽에 빈공간 발생  
> 원형큐로 해결!  
> 사실 그냥 기이이이다란 선형큐 쓰면됨

+ `front = rear = 0` : 초기 공백상태 
+ `front` 는 항상 비워둬야함  


|x|삽입위치|삭제위치|
|------|---|---|
|선형큐|rear += 1|front += 1|
|원형큐|rear = (rear + 1)%n|front = (front + 1)%n|

### 🦉원형큐 간단 구현🦉
```py
# 원형 큐 생성
q_size = 4
q = [0]*q_size
front = rear = 0

# 큐 삽입
rear = (rear + 1)%q_size
q[rear] = 'a'

rear = (rear + 1)%q_size
q[rear] = 'b'

rear = (rear + 1)%q_size
q[rear] = 'c'

# 큐 삭제
front = (front + 1)%q_size
print(q[front].pop())
```
### 🐧연결 큐 구조🐧
> + 기존의 배열을 이용한 자료구조는 데이터가 위치한 주소가 연결되어 있지만, 연결큐의 경우에는 데이터와 `다음주소`가 함께 저장되어있다.  
> + 이로인해 독립된 주소들에 데이터들을 저장할 수 있도록 하며, 각각의 데이터들은 `다음주소`를 통하여 연결 된 것 같이 작용한다. 
+ 공백큐생성시 `front` `rear`에는 `Null` 이 들어있다. 
+ 이하 내용생략
> 실무에서는 `linked list`형태가 사용되지만,  
> 알고리즘 문제풀이에서는 그냥 `배열` 사용하면 됨.

### 🐤deque🐤
```py
from collections import deque

q = deque()
q.append('a')
t = q.popleft()
```
```py
from collections import deque
li = []         # 매우느림
for i in range(1000000):
    li.append(i)
for i in range(10000):
    li.pop(0)
print('end')

lli = deque()   #  빠름
for i in range(1000000):
    lli.append(i)
for i in range(10000):
    lli.popleft()
print('end')
```
### 🐦우선순위 큐🐦
> 수면

### 🦃버퍼🦃
> 수면

### 🦇마이쮸🦇
+ 1 
+  12 123 1234
+  뭔 말이지 ?

![alt text](image.png)


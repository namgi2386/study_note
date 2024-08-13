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



#########################################
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


front = (front + 1)%q_size
print(q[front].pop())
```
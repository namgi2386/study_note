# front와 rear를 사용한 큐 구현

size = 10

q1= [0]*size 

front = rear = -1
# front : 첫원소가 있는 바로 이전자리
# rear : 마지막 원소 자리

for i in range(1,11):
    rear += 1
    q1[rear] = i*2
print(q1) # >>> [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(front , rear ) # >>> -1 9

# 원소 10개 삭제
for i in range(10):
    #삭제 전에 front + 1
    front += 1
    print(q1[front] , end=" ") # >>> 2 4 6 8 10 12 14 16 18 20
print()
print(q1) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] # q에는 요소가 남아있지만
print(front , rear ) # >>> 9 9    # front == rear : 큐가 비어 있다.





print('+++++++++++++++++++++++')
# 리스트 메서드를 사용해서 큐 구현
q = []

for i in range(10):
    q.append(i)

print(q) # >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10):
    print(q.pop(0) , end=" ") # >>> 0 1 2 3 4 5 6 7 8 9
print() # >>> [] # 이번엔 진짜 비어있다

print(q)
print(front , rear) # >>> 9 9 # 큐가 비어있다
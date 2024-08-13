class Node:
    def __init__(self,data):
        self.next = None
        self.prev = None
        self.data = data

    def __str__(self):
        return str(self.data)


class MyQ:
    def __init__(self):
        self.front = None
        self.rear = None


    # 삽입연산
    def enq(self,node):
        # 큐가 비었을 때의 삽입
        if self.is_empty():
            self.front = node
            self.rear = node
        else: # 큐에 원소가 있었을 때의 삽입
            self.rear.next = node
            node.prev = self.rear 
            self.rear = node

    # 삭제 연산
    def deq(self):
        # 삭제 원소 기억
        result = self.front
        # 연결헤제과정 (front뒤에 원소가 있을때가능)
        if result.next:
            # 큐의 맨앞은 front 바로 뒤 원소가 됨
            self.front = result.next
            # 삭제할 원소의 왼쪽과 오른쪽 연결 헤제
            result.next =None
            self.front.prev =None

        return 
    
    # 큐가 비었는지 확인
    def is_empty(self):
        return not self.front

q = MyQ

for i in range(1,11):
    node = Node(i)
    q.enq(node)

for i in range(10):
    print(q.deq() , end=" ")
print()
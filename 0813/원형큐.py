size = 10
cq = [0]*size # 사용가능한공간은 9칸 (나머지 1칸은 front의 빈칸전용)

front = rear = 0

def is_full():
    return (rear+1)%size == front

for i in range(1,11):
    if not is_full():
        rear = (rear+1)%size
        cq[rear] = i

print(cq) # >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(front , rear) # >>> 0 9
print()

# cq = [0]*size # 초기화
# front = rear = 0
# for i in range(1,12):
#     rear = (rear+1)%size
#     cq[rear] = i

# print(cq) # >>> [10, 11, 2, 3, 4, 5, 6, 7, 8, 9]
# print(front , rear) # >>> 0 1
# print()


for i in range(9):
    front = (front +1)%size
    print(cq[front] , end =" ")
print()

print(cq) # >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(front , rear) # 9 9


##################################################################################

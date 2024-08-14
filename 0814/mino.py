from collections import deque
import sys
sys.stdin = open('z3.txt', 'r')
import time
# T = int(input())
# for tc in range(1,T+1):
#     v= int(input())
tech =["|    @         @        |","|   @         @         |","|  @          <         |"]


print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)

n =10
s = 10
arr= ["|                       |" for _ in range(n)]
arr[2] = "|     @         @       |"
arr[7] = "|     -----------       |"
for t in range(3):
    time.sleep(0.5)
    arr[2] = tech[t]
    for i in range(n):
        print(arr[i])

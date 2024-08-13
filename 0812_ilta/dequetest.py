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
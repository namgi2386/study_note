def f_2():
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                for l in range(1,4):
                    print(f'{i} {j} {k} {l}')

def f():
    if len(s) == 4:
        print(*s)
        return
    for i in range(1,4):
        s.append(i)
        f()
        s.pop()

def g():
    if len(s) == 2:
        print(*s)
        return
    for i in range(1,4):
        if i not in s:
            s.append(i)
            f()
            s.pop()

s=[]
f_2()
print('---'*10)

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

print('---'*10)

def f_3(x):
    f_3(x+1)
# f_3(0)
# print('end')
'''
[Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
'''
def f(x):
    if x == 6:          # 종료조건
        return
    print(x, end=" ")   # 호출전
    f(x+1)
    print(x,end=" ")    # 종료후
f(1) # 1 2 3 4 5 5 4 3 2 1
print('---'*10)

path = []
def f_4(x):
    if x == 2:
        print(path , end=" ")
        return
    
    for i in range(3):
        path.append(i)
        f_4(x+1)
        path.pop()
f_4(0) # [0, 0] [0, 1] [0, 2] [1, 0] [1, 1] [1, 2] [2, 0] [2, 1] [2, 2]
print()

s = []
def f_5():
    if len(s) == 3:
        print(*s)
        s.pop()
        return
    
    for i in range(1,7):
        s.append(i)
        f_5()
f_5()
print('-*-'*10)

s = []
def f_6(x):
    if x ==3:
        print(*s)
        return
    for i in range(1,4):
        s.append(i)
        f_6(x+1)
        s.pop()
# f_6(0)
print('-*-'*10)

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

print('---'*10)

a = [10,20,30]
n = 3
b = [0]*n

def my_copy(x):
    if x ==n:
        return

    b[x] = a[x]
    f(x+1)
my_copy(0)
print(b)

# 재귀가 언제 끝날지 ==> a == b 일때, 혹은 인덱스가 n이 됐을때 
# 재귀를 하면서 뭐가 바뀌길 워하는가? == 몇번째 원소에 접근하는지!
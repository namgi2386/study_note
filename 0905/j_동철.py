import sys
sys.stdin = open('z5.txt' , 'r')

def fact(lev , property):
    global result

    if lev==n:
        result = max(result , property)
        return
    
    for i in range(n):
        if i not in s:
            s.append(i)
            if property * arr[lev][i] > result:
                fact(lev+1,property * arr[lev][i])
            s.pop()

for tc in range(1,int(input())+1):
    n = int(input())
    arr=[list(map(lambda x: float(x) ,input().split())) for _ in range(n)]

    s = []
    result = 0
    if tc<5:
        fact(0,1) # 레벨 , 확률
        result /=100.0
        print(f'#{tc} {result:.6f}')



'''
0.13 0.00  0.50
0.60 0.35 0.117











'''
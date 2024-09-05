import sys
sys.stdin = open('z1.txt' , 'r')

def fact(lev , price):
    global result
    if lev==n:
        result = min(result , price)
        return
    for i in range(n):
        if i not in s:
            s.append(i)
            if price + arr[lev][i] < result:
                fact(lev+1,price + arr[lev][i])
            s.pop()

for tc in range(1,int(input())+1):
    n = int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    s = []
    result = 0
    for i in range(n):
        result += sum(arr[i])
    fact(0,0)
    print(f'#{tc} {result}')
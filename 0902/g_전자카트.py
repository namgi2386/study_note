import sys
sys.stdin = open('z2.txt' , 'r')

def f():
    global result
    if len(s) == n-1:
        counts = arr[0][s[0]] + arr[s[n-2]][0]
        for i in range(n-2): 
            counts += arr[s[i]][s[i+1]]
        result = min(result , counts)
        return
    for i in range(1,n):
        if i not in s:
            s.append(i)
            f()
            s.pop()

for tc in range(1,int(input()) +1):
    n = int(input())
    s =[]
    arr =[list(map(int,input().split())) for _ in range(n)]
    
    result = 0
    for i in range(n):
        result += sum(arr[i])
    
    f()
    
    print(f'#{tc} {result}')
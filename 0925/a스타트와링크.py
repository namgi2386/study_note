import sys 
sys.stdin = open('z1.txt' , 'r')

def f(lev,A,B,a,b):
    global result
    if lev==n:
        if a != b:
            return
        total = 0
        for i in range(a):
                for j in range(b):
                    if i != j:
                        total += arr[A[i]][A[j]]
                        total -= arr[B[i]][B[j]]
        result = min(abs(total),result)
        return
    
    if a>(n//2) or b>(n//2):
        return

    f(lev+1 , A+[lev],B,a+1,b)
    f(lev+1,A,B+[lev],a,b+1)

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
result = int(2e9)
f(0,[],[],0,0)
print(result)

'''
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
'''
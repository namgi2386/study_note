import sys 
sys.stdin = open('z1.txt' , 'r')

def f(lev,A,B,cnt):
    global result
    if lev==n:
        if cnt :
            return
        total = 0
        for i in range(n//2):
                for j in range(n//2):
                    if i != j:
                        total += arr[A[i]][A[j]]
                        total -= arr[B[i]][B[j]]
        result = min(abs(total),result)
        return
    
    if lev>(n//2) and abs(cnt)>(n//2):
        return

    f(lev+1,A+[lev],B,cnt+1)
    f(lev+1,A,B+[lev],cnt-1)

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
result = int(2e9)
f(0,[],[],0)
print(result)
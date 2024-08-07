
def fibo1(n):
    global memo
    if n >= 2 and memo[n] == 0: # fibo(n)이 계산된적 없다면 실행됨.  >> 즉 이미 계산된 적 있다면 실행하지 않고 return으로감
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

n= 7
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
fibo1(n)
print(memo)

def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(35))

def fibo2(n):
    f = [0]*(n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2,n+1):
        f[i] = f[i-1] + f[n-2]
    return f[n]
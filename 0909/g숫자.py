
def f(lev , num):

    if lev == n:
        print(num)
        return
    
    for i in range(4):
        if opers[i] :
            opers[i] -= 1
            f(lev+1 , s(lev , num , i ))
            opers[i] += 1

def s(lev, num , i):
    if i==0:
        return num + numbers[lev]
    if i==1:
        return num - numbers[lev]
    if i==2:
        return num * numbers[lev]
    if i==3:
        return num // numbers[lev]


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    opers = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    
    f(0,numbers[0])

# a= -20
# b = 9
# print(a//b)
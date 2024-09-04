# import sys
# sys.stdin = open('z6.txt' ,'r')

# for tc in range(1,int(input()))

def f(lev):
    if lev==n:
        print(f'#1   {s_first}')
        print(f'#2                {s_second}')
        return
    
    for i in range(n):
        if lev%2==0 and i not in s_first and i not in s_second: # 짝수번째, 처음등장하는 인덱스
            s_first.append(i)
            f(lev+1)
            s_first.pop()
        elif lev%2==1 and i not in s_second and i not in s_first:
            s_second.append(i)
            f(lev+1)
            s_second.pop()


n = 4
s =[]
s_first  = []
s_second = []

f(0)


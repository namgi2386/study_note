import sys
sys.stdin = open('z1.txt','r')

def my_func():
    n = int(input())
    arr = list(map(int,input().split()))
    max_num = 0
    result = 0
    for x in arr[::-1]:
        if x > max_num:
            max_num = x 
        else :
            result += max_num - x 
    return result

T = int(input())
for tc in range(1,T+1):
    result = my_func()
    print(f'#{tc} {result}')
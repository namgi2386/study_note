import sys
sys.stdin = open('z1.txt','r')



def boo():
    n , m , k = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.append(0)
    boong_li = [0]*(13000*m)
    arr.sort()
    
    if arr[1] ==0:
        return 'Impossible'
    
    for i in range(1, 12000):
        boong_li[i] = (i//m)*k 
        # if i==30:
        #     print(boong_li[:29])
        if i in arr:
            if boong_li[i] < arr.index(i)+1:
                return 'Impossible'
    return 'Possible'

with open('check4.txt','a') as f:
    T = int(input())
    for tc in range(1,T+1):
        result = boo()
        r = f'#{tc} {result}'
        f.write(r + '\n')


# for tc in range(1,T+1):
#     result = boo()
#     print(f'#{tc} {result}')
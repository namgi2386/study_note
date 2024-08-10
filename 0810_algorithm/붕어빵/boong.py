import sys
sys.stdin = open('z1.txt','r')

def boo(tc):
    n , m , k = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.append(0)
    boong_li = [0]*(15000*m)
    arr.sort()
    # if tc == 998:
    #     print(arr)

    if arr[1] == 0:
        return 'Impossible'
    
    for i in range(1, 15000):
        boong_li[i] = (i//m)*k 

        if i in arr:
            if boong_li[i] < arr.index(i)+1:
                # if tc == 998:
                #     print(f'{boong_li[i]} {arr.index(i)+1}')
                return 'Impossible'
    return 'Possible'

with open('check4.txt','a') as f:
    T = int(input())
    for tc in range(1,T+1):
        result = boo()
        r = f'#{tc} {result}'
        f.write(r + '\n')

# T = int(input())
# for tc in range(1,T+1):
#     result = boo(tc)
#     r = f'#{tc} {result}'
#     print(r)
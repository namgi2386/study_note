import sys
sys.stdin = open('z6.txt' ,'r')


def f(lev):
    if lev==n:
        toatl_first.append(tuple(s_first[:]))
        toatl_second.append(tuple(s_second[:]))
        # print(f'{s_first} {s_second}')
        return
    
    for i in range(n):
        if lev%2==0 and i not in s_first and i not in s_second: # 짝수번째, 처음등장하는 인덱스
            if lev and i < s_first[lev//2 -1] : 
                continue
            s_first.append(i)
            f(lev+1)
            s_first.pop()

        elif lev%2==1 and i not in s_second and i not in s_first:
            if i < s_first[lev//2] :
                continue
            s_second.append(i)
            f(lev+1)
            s_second.pop()



for tc in range(1,int(input())+1):
    n = int(input())
    s_first  = []
    s_second = []

    toatl_first =[]
    toatl_second =[] 

    arr = [list(map(int, input().split())) for _ in range(n)]

    f(0)

    # print(toatl_first)
    # print(toatl_second)

    result = float('inf')
    for i in range(len(toatl_first)):
        tx =0
        ty =0
        for j in range(n//2):
            sx,sy = arr[toatl_first[i][j]] # 각 연결 지렁이의 좌표
            ex,ey = arr[toatl_second[i][j]]
            tx += (sx-ex)
            ty += (sy-ey)
        print(tx,ty)
        result = min( tx**2 +ty**2 , result )
    print(f'#{tc} {result}')


'''
[0, 2] [1, 3]
[0, 1] [2, 3]
[0, 1] [3, 2]
'''

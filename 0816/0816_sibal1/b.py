import sys
sys.stdin = open('z1.txt','r')

T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    even_arr=[]
    odd_arr=[]
    for i in range(n):
        for j in range(m):
            if (i%2 ==0 and j%2 == 0) or (i%2 !=0 and j%2 != 0):
                even_arr.append(arr[i][j])
            else:
                odd_arr.append(arr[i][j])
    se = set(even_arr)
    so = set(odd_arr)
    if '?' in se:
        se.remove('?')
    if '?' in so:
        so.remove('?')
    result = 'possible'
    if len(se)==2 or len(so)==2:
        result = 'impossible'
    if se and se == so:
        result = 'impossible'

    print(f'#{tc} {result}')
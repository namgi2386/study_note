import sys
sys.stdin = open('z1.txt','r')

def ww():
    for i in range(n):
        for j in range(m):
            if arr[i][j] in '#.':
                return (i,j ,arr[i][j])
    return (0,0,0)

T = int(input())

def val():
    if r[2] ==0:
        return 'possible'

    if (r[0]%2 ==0 and r[1]%2 == 0) or (r[0]%2 !=0 and r[1]%2 != 0): # 짝수자리에
        if r[2] == '#': # 샵있음
            if '.' in even_arr:
                return 'impossible'
            if '#' in odd_arr:
                return 'impossible'
        else: #   . 있음
            if '#' in even_arr:
                return 'impossible'
            if '.' in odd_arr:
                return 'impossible'
    else:# 홀수자리에
        if r[2] == '#':
            if '.' in odd_arr:
                return 'impossible'
            if '#' in even_arr:
                return 'impossible'
        else:
            if '#' in odd_arr:
                return 'impossible'
            if '.' in even_arr:
                return 'impossible'
    return 'possible'





for tc in range(1,T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    #r = ww()
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
    # print(f'{0} {se}')
    # print(f'{1} {so}')
    # result = val()
    print(f'#{tc} {result}')

#   0 1 2 3 4 5 6 7 8
# 0 # @ # @ # @ # @ #
# 1 @ # @ # @ # @ # @
# 2 #
# 3   #
# 4 #
# 5
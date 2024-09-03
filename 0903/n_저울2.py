import sys
sys.stdin = open('z5.txt' ,'r')

def soon():
    if len(s) == n:  # 순열의 길이를 n으로 맞춤
        total_arr.append(s[:])
        return
    for i in range(n):
        if i not in s:
            s.append(i)
            soon()
            s.pop()

def yang(my_arr, lev, left, right):
    global counts
    if lev == n:  # 레벨을 n까지 처리
        counts += 1
        return
    
    # left에 추가
    yang(my_arr, lev + 1, left + arr[my_arr[lev]], right)
    
    # right에 추가할 수 있는 경우에만 추가
    if arr[my_arr[lev]] + right <= left:
        yang(my_arr, lev + 1, left, right + arr[my_arr[lev]])

for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    s = []
    total_arr = []
    soon()
    tn = len(total_arr)
    counts = 0
    
    for i in range(tn):
        yang(total_arr[i], 0, 0, 0)
    print(f'#{tc} {counts}')

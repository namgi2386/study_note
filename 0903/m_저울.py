import sys
sys.stdin = open('z5.txt' ,'r')

def soon():
    if len(s) == n:
        total_arr.append(s[:])
        return
    for i in range(n):
        if i not in s:
            s.append(i)
            soon()
            s.pop()

def yang(my_arr , lev,left,right):
    global counts
    if lev==n:
        counts += 1
        return
    
    #left에 넣기
    hey = arr[my_arr[lev]]
    yang(my_arr,lev+1,left+hey,right)
    
    if hey+right <= left: # 0 1 2 
        # right에 넣기
        yang(my_arr,lev+1,left,right+hey)



for tc in range(1,int(input()) +1):
    n = int(input())
    arr = list(map(int, input().split()))
    s = []
    total_arr =[]
    soon()
    tn = len(total_arr)
    counts = 0
    # print(total_arr)
    
    for i in range(tn):
        yang(total_arr[i],0,0,0)
    print(f'#{tc} {counts}')
import sys
sys.stdin = open('z1.txt' , 'r')

def candidate(low , high):
    global result
    if low>high:
        result = high
        return
    
    mid = (low+high)//2

    counts = 0
    for i in range(n):
        counts += arr[i]//mid

    if counts < m:
        high = mid-1
    else:
        low = mid+1
    candidate(low,high)


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    result = 0
    candidate(1,max(arr))
    print(f'#{tc} {result}')
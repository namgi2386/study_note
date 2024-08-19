import sys
sys.stdin = open('z1.txt','r')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))

    zero_arr = [0]*n
    counts = 0

    for i in range(1,n+1): # 0 1 2 3 4 >> 12345 # 1, n+1
        if arr[i-1] != zero_arr[i-1]: # i-1
            h = 1
            while i*h <= n: # <=
                if zero_arr[i*h-1]: # -1
                    zero_arr[i*h-1] = 0
                else:
                    zero_arr[i*h-1] = 1
                h += 1
            counts += 1
            if zero_arr == arr:
                #print(tc ,zero_arr,arr)
                break
    print(f'#{tc} {counts}')

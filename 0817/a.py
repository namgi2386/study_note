import sys
sys.stdin = open('z1.txt' , 'r')

for tc in range(1,int(input())+1):

    arr = list(map(int,input().split()))
    counts =0
    for i in range(2):
        if arr[2-i] <= arr[1-i]:
            counts += (arr[1-i] - arr[2-i] + 1)
            arr[1 - i] = arr[2 - i] - 1
            if arr[1 - i] < 0 :
                counts = -1
                break

    
    print(f'#{tc} {counts}')


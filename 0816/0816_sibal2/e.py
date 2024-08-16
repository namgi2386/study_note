import sys
sys.stdin =open('z2.txt','r')

for tc in range(1,int(input())):
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

'''
4
3 2 1
1 2 3
3 5 5
5 6 6
'''
import sys
sys.stdin = open('z1.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    arr = [input() for _ in range(5)]
    m = 0
    for i in range(5):
        mm = len(arr[i])
        if mm > m:
            m = mm
    zarr = [['.']*m for _ in range(5)]
    for i in range(5):
        for j in range(len(arr[i])):
            zarr[i][j] = arr[i][j]


    print(f'#{tc} ',end="")
    for a in range(m):
        for b in range(5):
            if zarr[b][a] !='.':
                print(zarr[b][a],end="")
    print()



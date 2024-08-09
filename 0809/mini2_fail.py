import sys
sys.stdin = open('z1.txt','r')

lst = [1,2,3,4,5]
N = 5

def make_subset(idx , selected , n ):

    if idx == n :
        return
    subset = 0
    if selected[idx]
    selected[idx] = 1
    subset += arr[idx]
    make_subset(idx+1, selected , n )

    selected[idx] = 0
    make_subset(idx + 1, selected, n )


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    make_subset(0, [0]*N , N)
import sys
sys.stdin = open('z2.txt','r')

def tournament(i, j):
    if i == j :
        return i
    else:
        left = tournament(i, (i+j)//2)
        right = tournament((i+j)//2 + 1, j)

        if arr[left-1] + arr[right-1] == 4 and arr[left-1] !=2:
            if arr[left-1] == 1 : return left
            else: return right
        else :
            if arr[left-1] >= arr[right-1]: return left
            else : return right

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = tournament(1,N)
    print(f'#{tc} {result}')

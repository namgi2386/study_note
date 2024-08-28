import sys
sys.stdin = open('z2.txt' , 'r')

def hot_summer(t):
    global result1
    if t:
        hot_summer(left[t])
        hot_summer(right[t])
        result1 += str(arr[t-1])

def hot_hot_summer(t):
    global result2
    if t:
        hot_hot_summer(right[t])
        hot_hot_summer(left[t])
        result2 += str(arr[t-1])

for tc in range(1,int(input())+1):
    n = int(input())
    arr = list(map(int,input().split()))
    left = [0]*(n+1)
    right = [0]*(n+1)
    result1 =""
    result2 =""

    for i in range(2,n+1):
        if not left[i//2]:
            left[i//2] = i
        else:
            right[i//2] = i

    hot_summer(1)
    hot_hot_summer(1)
    if result1 == result2:
        print(f'#{tc} True')
    else:
        print(f'#{tc} False')

964-/3*

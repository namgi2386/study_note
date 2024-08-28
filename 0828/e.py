import sys
sys.stdin = open('z1.txt' , 'r')

def what(r):
    if num_arr[r] :
        return num_arr[r]
    else:
        if r*2+1 > n:
            return what(r*2)
        else:
            return what(r*2) + what(r*2 +1)


for tc in range(1,int(input())+1):
    n,m,r = map(int,input().split())
    num_arr = [0]*(n+1)

    for _ in range(m):
        temp_idx , temp_value = map(int, input().split())
        num_arr[temp_idx] = temp_value

    print(f'#{tc} {what(r)}')


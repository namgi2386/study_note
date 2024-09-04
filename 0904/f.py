import sys
sys.stdin =open('z3.txt' , 'r')


for tc in range(1,int(input())+1):
    n , m = map(int, input().split())
    a_arr = list(map(int,input().split()))
    b_arr = list(map(int,input().split()))
    counts = 0
    for i in range(m):
        if b_arr[i] in a_arr:
            counts += 1
    print(f'#{tc} {counts}')
import sys
sys.stdin = open('z1.txt' , 'r')
sys.stdout = open('o1_mine.txt' , 'w')

def c(t):
    global t_m , result
    if t_m == m :
        num = "".join(arr)
        result = max(result , int(num) )

        return
    t_m += 1
    for i in range(t,n):
        for j in range(i,n):
            arr[i] , arr[j] = arr[j] , arr[i]
            c(0)
            arr[i] , arr[j] = arr[j] , arr[i]





for tc in range(1,int(input())+1):
    num , m = map(int, input().split())
    arr = list(str(num))
    n = len(arr)
    t_m = 0
    result = 0
    c(0)
    print(f'#{tc} {result}')




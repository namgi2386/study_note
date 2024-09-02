import sys
sys.stdin = open('z1.txt' , 'r')
sys.stdout = open('o1_mine.txt' , 'w')

def c(t):
    global result
    if t == 5:
        num = "".join(arr)
        result = max(result , int(num) )
        return
    if t == m :
        num = "".join(arr)
        result = max(result , int(num) )
        return
    
    for i in range(t,n):
        for j in range(i,n):
            if i != j:
                arr[i] , arr[j] = arr[j] , arr[i]
                c(t+1)
                arr[i] , arr[j] = arr[j] , arr[i]


for tc in range(1,int(input())+1):
    num , m = map(int, input().split())
    arr = list(str(num))
    n = len(arr)
    result = 0

    c(0)
    
    print(f'#{tc} {result}')




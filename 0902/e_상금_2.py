import sys
sys.stdin = open('z1.txt' , 'r')


def c(t):
    global result
    if t == m :
        num = "".join(arr)
        result = max(result , int(num) )
        return
    
    for i in range(n-1):
        for j in range(i+1,n):
            arr[i] , arr[j] = arr[j] , arr[i]
            for k in range(t+1):
                if arr in visited[k]:
                    return

            visited[t].append(arr[:])
            c(t+1)
            arr[i] , arr[j] = arr[j] , arr[i]

for tc in range(1,int(input())+1):
    num , m = map(int, input().split())
    arr = list(str(num))
    n = len(arr)
    result = 0
    visited =[[] for _ in range(11)]

    # c(0)
    
    # print(f'#{tc} {result}')
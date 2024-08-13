import sys
sys.stdin = open('z2roll.txt' , 'r' )

T= int(input())

def roll(n,m,arr):
    front = -1
    rear = n-1
    q =[0]*(m+n)
    for i in range(n):
        q[i] = arr[i]
    
    for i in range(m):
        front +=1
        rear +=1
        q[rear]=q[front]
    return q[front+1]
        

for tc in range(1, T+1):
    n , m = map(int,input().split())
    arr = list(map(int,input().split()))

    result = roll(n,m,arr)
    print(f'#{tc} {result}')



import sys
sys.stdin = open('Z4.txt' , 'r' )

T = 10

def pa(arr):
    arr.append('s')
    front = 8
    rear = 7
    i = 0
    while True:
        rear = (rear + 1)%9
        front = (front + 1)%9
        arr[rear] = arr[front] -  (i%5 + 1) 
        if arr[rear] <= 0:
            arr[rear] = 0
            return arr,rear
        i+=1

for tc in range(1,T+1):
    input()
    arr = list(map(int,input().split()))
    result = pa(arr)

    idx = result[1]
    result_arr = result[0]

    print(f'#{tc}',end=" ")
    for h in range(8):
        print(result_arr[(idx + 2+h)%9],end=" ")
    print()
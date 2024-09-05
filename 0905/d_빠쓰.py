import sys
sys.stdin = open('z3.txt' , 'r')

def bossam(now , cnt):
    global result
    if now == n-1:
        result = min(result , cnt)
        return
    if cnt >= result:
        return
    mm = bus_arr[now]
    for i in range(mm,0,-1):
        if now + i <n:
            bossam(now+i , cnt +1)


for tc in range(1,int(input())+1):
    n , *bus_arr=list(map(int,input().split())) 
    result = n
    bossam(0,0)
    print(f'#{tc} {result-1}')

#[ 0 1  2   3    4    5 ]
#[[][][1,][1,2][2,3][2,4]]

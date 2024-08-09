T = int(input())
for tc in range(1,T+1):
    n , m , k = map(int,input().split())
    arr = [map(int, input().split())]
    boong_li = [0]*15000
    for i in range(1, 15000):
        if i%m == 0:
            boong_li[i] +=
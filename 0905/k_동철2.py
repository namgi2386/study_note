import sys
sys.stdin = open('z5.txt' , 'r')


for tc in range(1,int(input())+1):
    n = int(input())
    arr=[list(map(lambda x: float(x)/100 ,input().split())) for _ in range(n)]

    for i in range(n):




'''
[0,0,0,0] 2^4

0001 # 1 #  >> 1번이후 2번과제  a가 1번과제 b가 2번과제
0010 # 2 #  >> 2번이후 1번과제  a가 2번과제 b가 1번과제
0100
1000
0011 # 3

0 0 0 100

    1 2
a   10 6
b   9  4   
c   8  3



'''

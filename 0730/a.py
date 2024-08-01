import sys
sys.stdin = open("input.txt" , "r")

t = int(input())
for tc in range(1,t+1):

    n = input()
    li = list(map(int,input().split()))

    print(f'#{tc} {n}')
    print(li)


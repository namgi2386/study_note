# import sys
# sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    n = int(input())

    matrix = [list(map(int, list(input()))) for _ in range(n) ]
    c = (n//2) 
    result = 0
    for i in range(n):
        t = c - abs(c-i)
        for h in range( -1*t , t+1 ):
            # print(f'{i}행 {c+h}열' , end=", ")
            result += matrix[i][c+h]
    print(f'#{tc} {result}')

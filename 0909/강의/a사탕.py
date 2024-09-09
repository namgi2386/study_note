import sys
sys.stdin = open('z1.txt' , 'r')

for tc in range(1,int(input())+1):
    a,b,c = map(int,input().split())
    if b<2 or c<3 :
        print(f'#{tc} -1')
        continue
    eat = 0
    if b >=c:
        eat += b - (c-1)
        b =c-1
    if a >= b:
        eat += a - (b-1)
        a = b-1
    print(f'#{tc} {eat}')
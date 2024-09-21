import sys
sys.stdin =open('z1.txt','r')

def f(num):
    global anc
    if num<10:
        anc = num
        return
    f(num//10 + num%10)


for tc in range(1,int(input())+1):
    num = int(input())
    anc = 0
    f(num)

    print(f'#{tc} {anc}')

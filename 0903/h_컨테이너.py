import sys
sys.stdin = open('z2.txt' ,'r')

for tc in range(1,int(input())+1):
    n , m = map(int, input().split())
    kontainer,bus = [list(map(int,input().split())) for _ in range(2)]
    kontainer.sort(reverse=True)
    bus.sort(reverse=True)

    b_i = 0
    counts = 0
    for i in range(min(n,m)):
        if 0<= i+b_i :
            if kontainer[i]  <= bus[i+b_i]:
                counts += kontainer[i] 
            else:
                b_i -= 1

    print(f'#{tc} {counts}')


'''
kontainer [20, 19, 14, 14, 13, 11, 11, 10, 6, 5 ]
bus               [18, 18, 17, 17, 16, 15, 13, 9, 8, 5, 4, 1]

'''
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    arr = input()
    counts = 0
    plag = 0
    for i in arr:
        if i == '1' and plag == 0 :
            plag = 1
            counts += 1
        elif i == '0' and plag ==1 :
            plag = 0
            counts += 1
    print(f'#{tc} {counts}')

    
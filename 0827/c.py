import sys
sys.stdin = open('z2.txt' , 'r')

def how_are_you(t):
    if t:
        how_are_you(im_fine_thank_you[t])
        print(word[t] , end="")
        how_are_you(and_you[t])


for tc in range(1,11):
    n = int(input())
    word = {}
    im_fine_thank_you =[0]*101
    and_you =[0]*101
    for i in range(n):
        ar = list(input().split())
        arn = len(ar)
        p = int(ar[0])
        word[p] = ar[1]
        if arn >= 3:
            im_fine_thank_you[p] = int(ar[2])
        if arn == 4:
            and_you[p] = int(ar[3])
    

    print(f'#{tc} ',end="")
    how_are_you(1)
    print()

import sys
sys.stdin = open('s.txt' , 'r')

T = int(input())

for tc in range(1,T+1):
    p, a, b = map(int, input().split())
    # if a % 2 == 0:
    #     a -= 1
    # if b % 2 == 0:
    #     b -= 1
    li = [a, b]
    li_count =[0, 0]

    for i in range(2):
        start = 1
        end = p
        while start <= end:
            mid_idx = (start +end)//2
            if mid_idx == li[i] :
                break
            # if mid_idx %2 == 0:
            #     if mid_idx -1 == li[i]:
            #         break

            if mid_idx > li[i]:
                end = mid_idx
                li_count[i] += 1
            else:
                start = mid_idx
                li_count[i] += 1

    if li_count[0] < li_count[1]:
        print(f'#{tc} {li_count[0]}  {li_count[1]}       A')
    elif li_count[0] > li_count[1]:
        print(f'#{tc} {li_count[0]}  {li_count[1]}       B')
    else:
        print(f'#{tc} {li_count[0]}  {li_count[1]}       0')
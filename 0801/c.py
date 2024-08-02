import sys
sys.stdin = open('s.txt' , 'r')

T = int(input())

for tc in range(1,T+1):
    p, a, b = map(int, input().split())
    if a % 2 == 0:
        a -= 1
    if b % 2 == 0:
        b -= 1
    li = [a, b]
    li_count =[0, 0]

    for i in range(2):
        start = 1
        end = p
        while start <= end:

            mid_idx = (start +end)//2
            print(f'#{tc} {li[i]}는  {start}부터 {end}까지 {mid_idx}에 위치')
            if mid_idx % 2 ==0:
                mid_idx -= 1


            if mid_idx == li[i]:
                break
            elif mid_idx > li[i]:
                end = mid_idx
                li_count[i] += 1
            else:
                start = mid_idx
                li_count[i] += 1

# 1 400 401 200 199
# 1 199   200  100  99
# 199 400
# 1 5 6 3
# 1 7 8 4 3     12 34 56 78


    if li_count[0] < li_count[1]:
        print(f'#{tc} {li_count[0]}  {li_count[1]}       A')
    elif li_count[0] > li_count[1]:
        print(f'#{tc} {li_count[0]}  {li_count[1]}       B')
    else:
        print(f'#{tc} {li_count[0]}  {li_count[1]}       0')




# def binary_search(arr,n,key):
#     start = 0
#     end = n-1
#     while start <= end :
#         mid_idx = ( start + end )//2
#         if arr[mid_idx] == key:
#             return True
#         elif arr[mid_idx] > key:
#             end = mid_idx -1
#         else:
#             start = mid_idx +1
#     return False
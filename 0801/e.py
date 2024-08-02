import sys
sys.stdin = open('s.txt' , 'r')
T = int(input())

for tc in range(1,T+1):
    p, a, b = map(int, input().split()) # p 전체쪽수 a,b 찾을쪽수
    li = [a, b]
    book_num_lst = [ ] # 페이지 번호 리스트 ## [1,2,3,4,......400]
    for i in range(1,p+1):
        book_num_lst.append(i)

    li_count = [ ]

    for i in li:
        find_count = 0
        start = 0
        end = p
        while start <= end:
            mid = (start + end) // 2
            if book_num_lst[mid] == i:
                find_count += 1
                break
            elif book_num_lst[mid] > i:
                find_count += 1
                end = mid
            else:
                find_count += 1
                start = mid

        li_count.append(find_count)

    if li_count[0] < li_count[1]:
        print(f'#{tc} {li_count[0]}  {li_count[1]}       A')
    elif li_count[0] > li_count[1]:
        print(f'#{tc} {li_count[0]}  {li_count[1]}       B')
    else:
        print(f'#{tc} {li_count[0]}  {li_count[1]}       0')
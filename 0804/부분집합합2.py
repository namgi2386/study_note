T = int(input())

li = [1,2,3,4,5,6,7,8,9,10,11,12]
for tc in range(1, T+1):
    n , m = map(int,input().split()) # n개 더해서 m 만들수있는 경우의수 구하기
    count = 0
    for idx in range(1,1<<12): # 1~ 4000까지의 인덱스
        sub_li = []
        sub_sum = 0

        for j in range(12):
            if idx & (1<<j) :
                sub_sum += li[j]
                sub_li.append(li[j])
        
        if sub_sum == m and len(sub_li) == n :
            count += 1
    
    print(f'#{tc} {count}')



T = int(input())

li = [1,2,3,4,5,6,7,8,9,10,11,12]
for tc in range(1, T+1):
    n , m = map(int,input().split())
    count = 0
    for idx in range(1<<12):
        sub_li =[]
        sub_sum = 0
        for j in range(12):
            if idx & (1<<j):
                sub_li.append(li[j])
                sub_sum += li[j]
        if sub_sum == m and len(sub_li) == n:
            count += 1


li = [1,2,3,4,5,6,7,8,9,10,11,12]
for tc in range(1, T+1):
    n , m = map(int,input().split())
    count = 0
    for idx in range(1<<12):
        sub_li =[]
        sub_sum =0
        for j in range(12):
            if idx & (1<<j):
                sub_li.append(li[j])
                sub_sum += li[j]


    if sub_sum == m and len(sub_li) == n:
        count += 1
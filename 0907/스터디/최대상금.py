def recul(t):
    global max_price
    # 종료조건
    if t == n: # 최대 교환 횟수를 만족시켰으면
        max_price = max(max_price, int("".join(lst)))
        return
    # 재귀호출
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            lst[i], lst[j] = lst[j], lst[i] # 순서 바꾸기
            price = int("".join(lst))
            # 같은횟수만큼 바꿔서 같은 가격이면 이후에는 더이상 안해봐도 됨
            if (t,price) not in used:
                recul(t+1)
                used.append((t,price))
            lst[j], lst[i] = lst[i], lst[j] # 제자리로
 
T = int(input())
 
for tc in range(1,T+1):
    num, n = map(int,input().split()) # 숫자, 최대 교환 횟수
    lst = list(str(num)) 
    used = [] # 같은 상금이 있는지 확인용
    max_price = 0
    recul(0)
 
    print(f'#{tc} {max_price}')
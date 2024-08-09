lst = [1,2,3,4,5]


# idx : idx번째 자리에 있는 원소를 다른 우너소와 바꿔서 순열 만들어보기
# n 순열의 길이
def make_perm(idx , n):
    # 종료조건
    if idx == n:
        print(lst)
        return

    # 재귀조건
    # idx 번째 원소와 다른위치 ( j )에 있는 원소 자리바꿔보기
    # idx == j : 자리를 바꾸지 않겠다.
    # 자리를 바꿀 j를 선택해보자
    for j in range(idx , n ):
        # idx 번째 원소와 j번째 원소의 자리 교환
        lst[idx] , lst[j] = lst[j] ,  lst[idx]

        # idx + 1 번째 자리 바꾸러 가기
        make_perm(idx+1,n)

        # 자리 원래대로 되돌려 놓기
        lst[idx] , lst[j] = lst[j] ,  lst[idx]

make_perm(0,5)
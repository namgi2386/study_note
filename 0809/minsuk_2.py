lst = [1,2,3,4,5]
N = 5

# idx : 현재 순열의 i번째 자리에 올 원소를 선택하고 있다.
# selected : 순열 만들때 이전에 사용했던 원소 체크하기
# result : 지금까지 만든 순열
# n 순열 길이
def make_perm(idx , selected , result , n):

    # 종료조건
    if idx == n:
        print(result)
        return


    # 재귀호출

    # 현재순열의 idx 번째 자리에 놓을 원소선택
    # 이전에 고른적이 없는 원소를 자리에 놓아야함
    # 내가 고를 수 있는 원소는 lst 안에 있음
    # lst 인덱스 범위는 0~n-1
    for i in range(n):
        # i번째 원소를 이전에 고른 적이 없다면 순열의 idx 번째 자리에 i번 원소를 놓는다.
        if selected[i] == 0: # i번째 원소는 사용한적 없음
            # i번째 원소를 골랐다고 기록하고 넘어가야함
            selected[i] = 1
            result.append(lst[i])
            # idx+1 번째 자리에 넣을 원소 정하러가기
            make_perm(idx+1 , selected , result , n )

            # i번째 원소 원상복귀
            selected[i] = 0
            result.pop()
make_perm(0,[0]*N , [] , N)
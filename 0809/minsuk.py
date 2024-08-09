lst = [1,2,3,4,5]
li = []
N =5
S = 10
#print(lst)

# 0번째 원소를 고를까말까
# 1번쨰 원소를 고를까말까 ...


# selected : 내가 고른 원소 체크하기
# 만약 selected[x] == 1 : x번째 원소를 부분집합에 포함시킨상태
# n : 원소의 전체 개수
# s : 지금까지 구한 부분집합의 합

# idx번째 원소를 고를지 말지 선택하는 함수
def make_subset(idx , selected , n , s):
    global li

    # 가지치기 - 답이 될 가능성 없으면 진행하지 않기위해 사용
    if s > S:
        return

    # 종료조건
    if idx == n : # lst에는 인덱스가 n-1까지라서 idx == n라는건, 밖으로 나갔다는 뜻
        subset = []
        for i in range(n):
            if selected[i]:
                subset.append(lst[i])
        print(subset , end=" ")
        li.append(subset)
        return

    # 재귀호출 ( 여기서 부분집합을 만들 selected 만듬 )
        # idx 번째 원소에 대하여
        # 부분집합에 idx번째 원소를 포함할지 말지 정해
    selected[idx] = 1 # 넣었다면
    make_subset(idx+1, selected , n , s+ lst[idx]) # 다음원소 확인하러 가기

    selected[idx] = 0 # 넣지 않았다면 ( 넣었었으니까 다시빼기 )
    make_subset(idx + 1, selected, n , s)  # 다음원소 확인하러 가기

    # selected == [1,1,1,1,1] : 전부고른상태

make_subset(0, [0]*N , N , 0) # idx 0번부터 실행 , 빈칸N개짜리 만들어두고 시작
print()
print(len(li))
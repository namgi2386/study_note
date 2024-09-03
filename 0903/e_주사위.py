#idx 0 1 2 3 4
A = [1,2,3,4,5]

N=5
# idx : 부분집합에 넣을지 맣지 결정하는 원소의 위치

# 다음 재귀호출에서 이전 단계에서 골랐던 원소들을 알려줄 배열
# selected , visited , s 등
def subset(idx , selected):
    # 1. 종료조건
    if idx == N:
        print(selected)
        return
    # 2. 재귀호출
    # 각 단계에서 분기 수 만큼 재귀 호출
    # 부분집합에서의 분기는 idx번째 원소의 선택여부에따라 2가지로 나뉨

    # idx번째 원소 고른 이후 idx+1번째 원소를 선택하러 가기
    
    # selected.append(A[idx])
    # subset(idx+1,selected)
    
    subset(idx+1,selected + [A[idx]]) #이걸로한다면 되돌리지 않아도됨

    # 분기가 나눠질때 이전 선택에서 했던 일을 되돌려놔야함

    # idx번째 원소를 고르지 않고 idx +1번째 원소 선택하러가기
    
    subset(idx+1,selected)

subset(0,[])
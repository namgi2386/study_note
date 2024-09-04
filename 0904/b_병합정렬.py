# start : 시작위치
# end : 끝위치
def merge_sort(start , end):
    # 원소가 하나 남았을 때 중단하기
    if start == end-1:
        return start,end

    # 재귀호출 
    # 분할하여 왼쪽 오른쪽 나눔
    mid = ( start + end )//2        
    # 단, 여기서 overflow 발생 가능 start//2 + end//2 == start + (end-start)//2

    left_start, left_end = merge_sort(start , mid)
    right_start, right_end = merge_sort(mid , end)

    return merge(left_start, left_end , right_start, right_end)


def merge(ls,le,rs,re):

    n = re - ls 
    result = [0] * n

    idx = 0 # 왼쪽 오른쪽 중 작은수를 놓을 자리를 idx에 저장

    l,r = ls,rs # 왼쪽의시작점과 오른쪽시작점만 비교하면됨

    while l < le  and r < re:
        if arr[l] < arr[r]:
            result[idx] = arr[l]
            l += 1
            idx += 1
        else:
            result[idx] = arr[r]
            r += 1
            idx += 1

    while l < le:
        result[idx] = arr[l]
        l += 1
        idx += 1

    while r < re:
        result[idx] = arr[r]
        r += 1
        idx += 1

    for i in range(n):
        arr[ls+i] = result[i]


arr = [69, 10, 30, 2, 16, 8, 31, 22]
merge_sort(0,8)
print(arr)

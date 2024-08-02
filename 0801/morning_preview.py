# def binary_search(lst,n,key):
#     # lst : 검색 리스트
#     # n : 리스트 길이
#     # key : 찾는값
#     start = 0 # 시작위치 ( 갱신하며 변경할 예정 )
#     end = n-1 # 끝 위치  ( 갱신하며 변경할 예정 )
#     while start <= end : # start와 end가 교차됨 == 못찾음 == return false
#         mid_idx = ( start + end )//2
#         if lst[mid_idx] == key:
#             return True
#         elif lst[mid_idx] > key:
#             end = mid_idx -1
#         else:
#             start = mid_idx +1
#     return False
#
# def prectice_defualt(lst,n=-1):
#     if n == -1:
#         n = len(lst)
# li = [1,3,5,6]
# prectice_defualt(li)
# prectice_defualt(li,3)


def selection_sort(arr , n):
    for i in range(n-1):
        min_idx =i
        for j in range(i+1,n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx], arr[i]

A = [2,5,7,3,4]
selection_sort(A,len(A))
print(A)
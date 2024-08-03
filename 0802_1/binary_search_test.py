def binary_search(target, data):
    #data.sort()
    start = 0 			# 맨 처음 위치
    end = len(data) - 1 	# 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2 # 중간값

        if data[mid] == target:
            return mid 		# target 위치 반환

        elif data[mid] > target: # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return mid

data = [4,7,4,3,7,9,9,6,5,7]
data.sort()
target = 8
t = binary_search(target,data)
if data[t] < target:
    t += 1 
# target의 인덱스를 반환
# target이 없다면, target이 들어갈 자리의 인덱스
print(t)
print([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print(data)

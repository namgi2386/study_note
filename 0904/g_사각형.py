
def binary_search(target):
    low = 0
    high = n

    while low <= high:
        mid = (low + high) // 2

        if mid*mid == target:
            return mid
        elif mid*mid > target:
            high = mid - 1
        else:
            low = mid + 1
    return 0


for tc in range(1,int(input())+1):
    n= int(input())
    print(f'#{tc} {binary_search(n)}')

    
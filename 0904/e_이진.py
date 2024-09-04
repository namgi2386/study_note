import sys
sys.stdin =open('z3.txt' , 'r')

def lightandsolt(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = lightandsolt(left_arr)
    right_arr = lightandsolt(right_arr)
    return myfriend(left_arr,right_arr)

def myfriend(left , right):
    result = [0]*(len(left) + len(right))
    l=r=0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1
    while l < len(left):
        result[l+r] = left[l]
        l += 1
    while r < len(right):
        result[l+r] = right[r]
        r+= 1
    return result

def podo(from_arr ,target):
    global bottom
    left = 0
    right = n-1
    cnt =0 
    while left <= right:
        mid = left + (right-left)//2
        cnt += 1
        if from_arr[mid] == target:
            return True
        elif from_arr[mid] > target:
            if bottom == 0 or bottom == 1 :
                bottom = 2
            elif bottom == 2:
                bottom = 3
            right = mid -1
        else:
            if bottom == 0 or bottom == 2 :
                bottom = 1
            elif bottom == 1:
                bottom = 3
            left = mid +1
    return False

for tc in range(1,int(input())+1):
    n , m = map(int, input().split())
    a_arr = list(map(int,input().split()))
    b_arr = list(map(int,input().split()))
    a_arr = lightandsolt(a_arr)
    
    counts = 0
    for i in range(m):
        bottom = 0
        if podo(a_arr , b_arr[i]) and bottom != 3:
            counts += 1
    print(a_arr)
    print(f'#{tc} {counts}')








'''
1
3 5
3 2 1
1 3 7 8 9
'''
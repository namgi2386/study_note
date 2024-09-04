import sys
sys.stdin =open('z2.txt' , 'r')


def inner_sort(left , right):
    pivot = arr[left]
    i = left +1
    j = right

    while i<=j:
        while i<=j and arr[i] <= pivot :
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j

def q_sort(l,r):
    if l < r:
        pivot = inner_sort(l,r)
        q_sort(l,pivot-1)
        q_sort(pivot+1, r)

n =1000000
arr =list(map(int, input().split()))
# arr.sort()
q_sort(0,n-1)
print(arr[n//2])
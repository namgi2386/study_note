def selection_sort(a):
    arr = map(int, a.split() )
    print(arr)
    n = len(arr)
    for i in range(n-2):
        min_idx =i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx], arr[i]

A = '1 2 3 4 5 6 7 8 9 10'
selection_sort(A)
print(A)

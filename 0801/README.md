# 🎄검색🎄

---

> 순차검색 , 이진검색 , 해쉬 , 등
> 
> 일렬로 되어있는 자료검색 == 간단 + 비효율

> 정렬 여부에 따라 다른결과

## 🙋‍♀️정렬되지 않은 경우
#### 검색횟수 : `(n+1)/2` ( 평균적으로 절반쯤에서 발견 )
#### 시간복잡도 : `O(n)`
> 아래의 두가지 방법 모두 할 줄 알아야함
```python
def for_search(arr,n,key):
    for i in range(n):
        if arr[i] = 'key' :
            return i
    return -1
```
#### `핵심코드` 🦊`i < n and arr[i] != 'key'`🦊
```python
def sequential_search(arr,n,key):
    i = 0
    while i < n and arr[i] != 'key' : 
        # 키 찾거나 배열끝나야 탈출
        i += +1
    if i < n :
        return i # 현재 인덱스값 반환
    else :
        return -1
```
## 🙋‍♀️정렬됨 (오름차순)
> 배열 내 답이 있는경우에는 정렬되지 않았을때와 동일
> 
> 답이없을때는 중간쯤가다가 답이없음을 알고 검색중단가능

#### `핵심코드` 🦊`i < n and arr[i]<key`🦊
```python
def sequetial_search_that_sorted(arr,n,key):
    i = 0 
    while i < n and arr[i]<key :
        i +=1
    if i<n and arr[i] == key :
        return i
    else : 
        return -1
```
#### `추가개념` ( 단축평가를 고려했을 때 두가지 코드 비교 )
> `i < n and arr[i]<key`

> `arr[i]<key and i < n `

## 🦩 이진검색 binary search 

#### `개념`
    + 일단 중앙 선택
        + 찾는값과 크기비교
        + 절반제거
        
    + 나머지 구간에서의 중앙선택
        + 찾을때까지 반복 
#### `이런느낌`
```python
while 남은구간 있으면 :
    mid = start + end // 2
    if arr[mid] == key
        return mid

    if arr[mid] < key :
        start = mid +1
    else :
        end = mid - 1
```
#### `정답코드`
```python
def binary_search(arr,n,key):
    start = 0
    end = n-1
    while start <= end :
        mid_idx = ( start + end )//2
        if arr[mid_idx] == key:
            return True
        elif arr[mid_idx] > key:
            end = mid_idx -1
        else:
            start = mid_idx +1
    return False
```
> 재귀함수를 이용하는 방법 있긴함
#### `추가개념`
> 이진트리 + 자료구조
> + 오늘배우는 배열형태의 이진탐색에서 검색은 빠르지만
> + 삽입 삭제는 느리다 (append같은느낌?)
> + 이진트리자료구조에서는 삽입삭제또한 빠르게 개선된 형태가 존재
> + 데이터베이스 인덱스가 이진탐색트리구조이다.
> + 나중에 배움

## 🐓 선택정렬 selection sort

#### `개념`
> + 정렬되지 않은 배열
> + 최솟값 찾기
> + 맨 앞 위치 얘랑 자리교체
> + 반복
#### 시간복잡도 : `O(n)`

#### `이런느낌`
```python
def selection_sort(arr): # 최솟값의 인덱스 찾기
    n = len(arr)
    mid_idx = 0
    for i in range(n):
        if arr[mid_idx] > arr[i]:
            mid_idx = i
```
#### `정답코드`
```python
def selection_sort(arr): # return 없음
    n = len(arr)
    for i in range(n-1):
        mid_idx = 0
        for j in range(i+1,n):
            if arr[mid_idx] > arr[j]:
                mid_idx = j
        arr[i],arr[mid_idx] = arr[mid_idx], arr[i]
```
## 🦌 선택정렬 실습
```python
def selection_sort(arr , n):
    for i in range(n-2): # [ [0][1][...][n-2][n-1] ]
        min_idx =1
        for j in range(i+1,n): #[ [...][i][i+1][...][n-1] ]
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx], arr[i]
A = [2,5,7,3,4]
selection_sort(A,len(A))
print(A)
```

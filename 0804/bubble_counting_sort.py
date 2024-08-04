# arr = [1,6,4,8,5]
# n = 5
# for i in range(n-1,0,-1):
#     for j in range(i): 
#         if arr[j] > arr[j+1]: 
#             arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [1,6,4,8,5,1,1]
n = 7
k = max(arr) # 8

temp = [0]*n
counts = [0]*(k+1)

for i in range(n):
    x = arr[i] # 숫자하나씩 가져와서
    counts[x] += 1 # counts에 갯수세기
#print(counts) >>> [0, 3, 0, 0, 1, 1, 1, 0, 1]
for i in range(1,k+1): # 1 ~ k 까지
    counts[i] += counts[i-1] # 누적합
#print(counts) >>> [0, 3, 3, 3, 4, 5, 6, 6, 7]

for i in range(n-1,-1,-1):
    x = arr[i] # 숫자하나씩 가져와서
    counts[x] -= 1 # 그 숫자의 갯수 하나씩 줄임
    temp[counts[x]] = arr[i] # 빈 배열에 넣기
print(temp) # [1, 1, 1, 4, 5, 6, 8]



arr =[1,6,4,8,5,1,1]
n = 7
k = max(arr)
counts = [0]*(k+1)
temp = [0]*n

for i in range(n):
    counts[arr[i]] +=1
for i in range(k+1):
    counts[i] += counts[i-1] 
for i in range(n+1,-1,-1):
    counts[arr[i]] -= 1
    temp[counts[arr[i]]] = arr[i]








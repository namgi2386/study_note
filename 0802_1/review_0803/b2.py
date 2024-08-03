# t = int(input())
# for tc in range(1,t+1):
arr = [3,6,2,3,7,9]
#p,n = map(int,input().split())
n =7
arr.sort() # [2,3,3,6,7,9]
while start <= end :
    start = 1
    end = len(arr)

    mid = (start+end)//2

    if mid == n:
        break

    if mid > n :
        end = mid -1
    if mid < n :
        start = mid +1
print(mid)

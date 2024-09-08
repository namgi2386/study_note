# import sys
# sys.stdin = open('z2.txt' , 'r')

# #리스트 값 중 2개 뽑기 순열
# def mine(n,s,lev):
#     if lev==2:
#         print(s)
#         return
#     for i in range(1,n+1):
#         if i not in s:
#             s.append(i)
#             mine(n,s,lev+1)
#             s.pop()
# mine(4,[],0)
# print('--'*10)



# # 몇개 뽑아야할지 정해져있으니까. 
# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i != j:
#             print((i,j))
# print('--'*10)

# # n개의 값을 2개의 리스트로 구분한다

# def cook(i,a,b):
#     if len(a) > n//2 or len(b)>n//2:
#         return
#     if i==n:
#         print(a,b)
#     cook(i+1,a+[i],b)
#     cook(i+1,a,b+[i])
# n=4
# cook(0,[],[])

# 종료조건 추가
def cook(i,a,b):
    global result
    if len(a) > n//2 or len(b)>n//2:
        return
    if i==n:
        left = 0
        right = 0
        for i in range(n//2):
            for j in range(n//2):
                if i != j :
                    left += arr[a[i]][a[j]]
                    right += arr[b[i]][b[j]]
        result = min(result , abs(left - right))
        return

    cook(i+1,a+[i],b)
    cook(i+1,a,b+[i])


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 1e9
    cook(0,[],[])
    print(f'#{tc} {result}')
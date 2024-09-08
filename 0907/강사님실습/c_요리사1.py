
def devide(t):
    global result
    if len(s) ==n//2:
        left = s
        right =[]
        temp_diff = 0
        for i in range(n):
            if i not in s:
                right.append(i)
        if left[0] < right[0]:
            for i in range(len(total_li)):
                r =left[total_li[i][0]]
                c = left[total_li[i][1]]
                temp_diff += arr[r][c] + arr[c][r]
                r =right[total_li[i][0]]
                c = right[total_li[i][1]]
                temp_diff -= arr[r][c] + arr[c][r]
            result = min(result , abs(temp_diff))
        return 
    
    for i in range(t,n):
        if i not in s:
            s.append(i)
            devide(i)
            s.pop()


def inner(t):
    if len(s_in)==2:
        total_li.append(s_in[:])
        return
    for i in range(t,n//2):
        if i not in s_in:
            s_in.append(i)
            inner(i)
            s_in.pop()



for tc in range(1,int(input())+1):
    n = int(input())
    arr =[list(map(int, input().split())) for _ in range(n)]
    s=[]
    s_in= []
    left =[]
    right =[]
    total_li =[]
    result = 1e9
    inner(0)
    devide(0)
    print(f'#{tc} {result}')




# 리스트 절반으로 나누는 경우의 수
# 절반에 대한 조합

# n=4

# s=[]
# s_in= []
# left =[]
# right =[]
# total_li =[]
# result = 1e9
# # arr =[
# # [0, 5, 3, 8],
# # [4, 0, 4, 1],
# # [2, 5, 0, 3],
# # [7, 2, 3, 0],]
# inner(0)
# devide(0)
# print(result)




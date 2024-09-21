# 1. 알지비
# 2. 뱀 업로드
# 3. 선수과목 업로드
# 4. 1로만들기

def dfs(lev, num , pre_col):
    global result
    if lev==n:
        result = min(result, num)
        return
    
    for now_col in range(3):
        if now_col != pre_col:
            dfs(lev +1 , num + arr[lev][now_col] , now_col)

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
result =1e9
dfs(0,0,-1)

print(result)





# 우선 가로2칸으로 탐색할건데 범위는 
    # n까지
    # m-1까지
    # temp_sum = 2칸의 합 변수에 저장

# dr dc 이용해서 10개방향 순회하며 2개뽑아서 계산 할 예정
# is_valid 사용해서 가능여부 판단 
    # 가능하다면 선택하는걸로하고 재귀 순회

# 종료조건은 
    # 2개 뽑았을때 리턴하고 그다음꺼 뽑아보기

dr =[-1,1,0,0]
dc =[0,0,-1,1]

def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<m

def f(lev , num , i,j,visited,pi,pj):
    global max_num
    if lev==4:
        max_num = max(max_num , num)
        return

    for d in range(4):
        nr = i + dr[d]
        nc = j + dc[d]
        if is_valid(nr,nc) and (nr,nc) not in visited:
            if lev==2 and (nr==pi+2 or nc==pj+2):
                num_1 = 0
                if nr ==pi+2:
                    if is_valid(i,j+1):
                        num_1 = arr[i][j+1]
                    if is_valid(i,j-1):
                        num_1 = arr[i][j-1]
                if nc ==pj+2:
                    if is_valid(i+1,j):
                        num_1 = arr[i+1][j]
                    if is_valid(i-1,j):
                        num_1 = arr[i-1][j]
                max_num = max(max_num , num+arr[nr][nc]+num_1)
                num_1 = 0

            f(lev+1,num+arr[nr][nc] , nr,nc,visited +[(nr,nc)],pi,pj)


n , m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

max_num = 0
for i in range(n):
    for j in range(m):
        num = arr[i][j]
        f(1, num ,i,j,[(i,j)],i,j) 
print(max_num)
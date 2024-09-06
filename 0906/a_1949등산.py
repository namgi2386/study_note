import sys
sys.stdin = open('z1.txt' , 'r')

# 완전탐색
# dfs stack 사용
# 4개방향
# isvalid , visited 사용
# visited에 최대길이 기록
# 끝지점에서 땅파기 해보기 

def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n

dr =[-1,0,1,0]
dc =[0,1,0,-1]

def maount(i,j,lev,flag):
    global temp_max
    this_position = arr[i][j]
    for d in range(4):
        nr = i + dr[d]
        nc = j + dc[d]
        if is_valid(nr,nc) and this_position < arr[nr][nc] and not visited[nr][nc]: # 등산
            visited[nr[nc]]
            temp_max = max(maount(nr,nc,lev+1,flag), temp_max)
    else:
        if flag and is_valid(nr,nc) and arr[nr][nc] > this_position - dick:
            my_dick = arr[nr][nc] - this_position +1
            flag = 0
            arr[nr][nc] -= my_dick
            temp_max = max(maount(nr,nc,lev+1,flag), temp_max)
        else:
            return lev


3
7 9  18 


for tc in range(1,int(input())+1):
    n,dick = map(int , input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            visited =[[0]*n for _ in range(n)]
            visited[i][j] = 1
            temp_max = 0
            maount(i,j,1,1)








#39분
import sys
sys.stdin = open('z1.txt' , 'r')

dr =[-1,0,1,0]
dc =[0,1,0,-1]

def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n

def solve(r,c,flag , visited , lev , position_high):
    global result
    result = max(result , lev)

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if is_valid(nr,nc) and (nr,nc) not in visited :
            if arr[nr][nc] < position_high:
                visited.append((nr,nc))
                solve(nr,nc,flag,visited,lev+1 , arr[nr][nc])
                visited.pop()
            elif  flag:
                for curt in range(1,m+1):
                    if arr[nr][nc]-curt < position_high:
                        visited.append((nr,nc))
                        solve(nr,nc,False,visited,lev+1 , arr[nr][nc]-curt)
                        visited.pop()

for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n) ]

    maximum_high = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > maximum_high:
                start_point = [(i,j)]
                maximum_high = arr[i][j]
            elif arr[i][j] == maximum_high:
                start_point.append((i,j))
    
    result = 0
    for r,c in start_point:
        solve(r,c , True , [(r,c)] , 1 , maximum_high)
    
    print(f'#{tc} {result}')
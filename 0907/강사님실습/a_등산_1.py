import sys
sys.stdin = open('z1.txt' , 'r')

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n

def solve(r,c,visited,position_high , flag , lev):
    global result

    result = max(result,lev)

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if is_valid(nr,nc) and  (nr,nc) not in visited:
            if arr[nr][nc] < position_high :
                visited.append((nr,nc))
                solve(nr,nc,visited , arr[nr][nc] , flag , lev+1 )
                visited.pop()
            elif flag:
                for cuth in range(1,k):
                    if arr[nr][nc] -cuth < position_high:
                        visited.append((nr,nc))
                        solve(nr,nc,visited,arr[nr][nc]-cuth, False,lev+1)
                        visited.pop()


for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    # start_point 봉우리 리스트
    maximum_high = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > maximum_high:
                start_point =[(i,j)]
                maximum_high = arr[i][j]
            elif arr[i][j] == maximum_high:
                start_point.append((i,j))

    
    result = 0
    for r,c in start_point:
        solve(r,c , visited=[(r,c)] , position_high=maximum_high , flag=True ,lev=1 )
    
    print(f'#{tc} {result}')
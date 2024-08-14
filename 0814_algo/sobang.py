
dr=[-1,1,0,0]
dc=[0,0,-1,1]

def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n

def burn(maze):
    visited =[ [0]*n for _ in range(n)]

    q = []
    q.append((pr,pc))
    
    red_result =[]
    for rs in range(len(red_spot)): # 각 소화기 찾으러가기
        visited[pr][pc] = 0
        while q:
            r,c = q.pop(0)
            if maze[r][c] == 'A':
                maze[r][c] = '_'
                red_result.append((rs,r,c,visited[r][c]))
                break
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if is_valid(nr,nc) and not visited[nr][nc] and maze[nr][nc] in 'A_' :
                    q.append((nr,nc))
                    visited[nr][nc] = visited[r][c] + 1
    return red_result # [(0, 4, 6, 2), (1, 1, 4, 3), (2, 3, 2, 5)]

def fire(red):
    rr = red[1]
    rc = red[2]
    red_result = red[3]
    visited2 =[ [0]*n for _ in range(n)]

    q = []
    q.append((rr,rc))
    
    while q:
        r,c = q.pop(0)
        if maze[r][c] == '$':
            return red_result + visited2[r][c]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr,nc) and not visited2[nr][nc] and maze[nr][nc] in '$_':
                q.append((nr,nc))
                visited2[nr][nc] = visited2[r][c] + 1

T = 1
for tc in range(1,T+1):
    n = int(input())
    maze = [list(input()) for _ in range(n)]
    pr,pc = map(int,input().split()) # 현재위치

    red_spot =[] # 소화기 위치
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 'A':
                red_spot.append((i,j))
            if maze[i][j] == '$':
                fire_spot = (i,j) # 불 위치

    red_result = burn(maze)
    result = 10000000
    for i in range(len(red_result)):
        r = fire(red_result[i])
        if r < result:
            result = r

    #print(red_result)
    print(result)

'''
8
________
____A___
####____
__A#____
___#__A_
_#______
__###___
_$______
4 4
'''
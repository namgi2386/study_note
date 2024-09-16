from collections import deque

def turn_snake(idx): # 방향전환
    global d
    if rotation[idx] == 'D':
        d = (d+1)%4
    else:
        d = (d+3)%4




n = int(input()) # n*n행렬
m = int(input()) # 사과개수
board = [[0]*(n) for _ in range(n)]
apples = [] # 사과 좌표
for _ in range(m):
    x,y = map(int,input().split())
    xx = x - 1
    yy = y - 1
    apples.append((xx,yy))
    board[xx][yy] = 1

l = int(input()) # 방향 전환 횟수
times = [] # 시간 정보
rotation = [] # 방향 전환 정보
for _ in range(l):
    t,c = input().split()
    times.append(int(t))
    rotation.append(c)

#    상 우 하 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

snake = deque() # 뱀의 머리위치 저장
snake.append((0,0))
r,c = 0,0 # 뱀 시작위치
d = 1 # 시작시 뱀의 이동방향
cnt = 0 # 게임 진행 시간

# finish = True
for _ in range(10001): # 게임시간은 최대 10000을 넘지 않으니까...
    cnt += 1
    nr,nc = r+dr[d], c+dc[d]
    # 벽과 부딪히지 않고 뱀의 몸과도 부딪히지 않는다면
    if 0<=nr<n and 0<=nc<n and (nr,nc) not in snake:
        # 사과가 있으면
        if board[nr][nc] == 1: 
            # 사과 먹고 snake에 append하고 pop안해도 됨
            board[nr][nc] = 0
            snake.append((nr,nc))
            r,c = nr,nc
            
        else: # 사과가 없으면 
            snake.append((nr,nc))
            r,c = nr,nc
            snake.popleft()       
    else: # 벽과 부딪히고 뱀의 몸과도 부딪히면 종료
        break

    if cnt in times:# 방향전환을 해야되면
        turn_snake(times.index(cnt))
        
print(cnt)

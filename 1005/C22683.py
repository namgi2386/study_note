import sys
sys.stdin = open('z1.txt' , 'r')

from collections import deque 

dr = [-1,0,1,0]
dc = [0,1,0,-1]
def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n

T = int(input())
for tc in range(1,T+1):
    n,maximum_treecut = map(int,input().split())
    arr = [list(input()) for _ in range(n)]

    visited = [   [[100]*(maximum_treecut+1) for _ in range(n) ]    for _ in range(n)   ] # 3차원배열
    # 각지점(r,c)의 최소 이동횟수를 저장할건데,
    # 나무벤 횟수에 따른 이동횟수를 따로 저장해 줘야댐
    # 즉 3,5 지점의 visited 값이 [10,7,6] 이라면, 
        # 나무를 0회 베고 (3,5)에 도착하기 위한 최소 이동횟수는 10 
        # 나무를 1회 베고 (3,5)에 도착하기 위한 최소 이동횟수는 7 
        # 나무를 2회 베고 (3,5)에 도착하기 위한 최소 이동횟수는 6 

    result = int(1e9)

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X':
                sr , sc = i,j           # 시작지점

    q = deque()
    q.append((sr,sc,0 ,0 , 0)) # 위치 , 나무벤횟수 , 이동거리 , 현재방향
    visited[sr][sc][0] = 0      

    while q :
        r,c,tree , cnt , d = q.popleft()  # 위치 , 나무벤횟수 , 이동거리 , 현재방향

        if arr[r][c] == 'Y':            # 종료조건
            result = min(result , cnt)
        
        if cnt > result :               # 가지치기
            continue

        for dt in range(4):  

            
            now_move_cnt = cnt                  # 현재 이동횟수
            now_treecut = tree                  # 현재 나무벤 횟수


            if dt ==1 or dt==3: # 90도 회전
                now_move_cnt += 1               # 90도 회전은 이동횟수 1추가 
            elif dt==2:         # 180도 회전
                now_move_cnt += 2               # 180도 회전은 이동횟수 2추가 
            now_move_cnt += 1        # 전진

            now_d = (d + dt)%4                  # 0 1 2 3 반복하기 위해서 %4 해줌
            nr = r + dr[now_d]
            nc = c + dc[now_d]

            if is_valid(nr,nc):
                if arr[nr][nc] in ('G','Y') :
                    if visited[nr][nc][now_treecut] > now_move_cnt:
                        visited[nr][nc][now_treecut] = now_move_cnt
                        q.append((nr,nc, now_treecut , now_move_cnt, now_d))

                elif arr[nr][nc] == 'T' and now_treecut <maximum_treecut:
                    now_treecut += 1
                    if visited[nr][nc][now_treecut] > now_move_cnt:
                        visited[nr][nc][now_treecut] = now_move_cnt
                        q.append((nr,nc, now_treecut , now_move_cnt, now_d))

    for i in range(n):
        print(visited[i])
    if result == int(1e9):
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {result}')

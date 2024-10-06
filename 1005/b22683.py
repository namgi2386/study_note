import sys
from collections import deque 
sys.stdin = open('z1.txt' , 'r')

dr = [-1,0,1,0]
dc = [0,1,0,-1] # 시계방향

def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n


T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = [list(input()) for _ in range(n)]
    visited = [[[ int(100)]*(m+1) for _ in range(n) ] for _ in range(n)]


    result = int(1e9) # 여기에 결과 저장

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X':
                sr , sc = i,j

    q = deque()
    # sr 시작 row값
    # sc 시작 col값
    # 0 : 나무벤 횟수
    # 0 : 현재 이동횟수
    # 0 : 현재바라보는 방향 (dr,dc참고)
    q.append((sr,sc,0 ,0 , 0)) # 시작위치와 나무벤 횟수(0~m) , 이동횟수 , 현재바라보는방향을 가지고 시작
    visited[sr][sc][0] = 0


    while q :
        r,c,tree , cnt , d = q.popleft() 

        # 종료조건
        if arr[r][c] == 'Y':
            result = min(result , cnt)
        
        # 가지치기
        if cnt > result :
            continue

        # 애초에 dr , dc를 시계방향으로 설정해뒀다. 
        # d 의 초기값은 0 
        # (d + dt)%4 에 의해서 왼쪽이동 전진 오른쪽이동 구현
        # dt = 1 일때, 오른쪽 회전후 전진 
        # dt = 0 일때, 전진
        # dt = 3 일때, 왼쪽 회전후 전진
        # dt = 2 일때, 뒤로돌기
        for dt in range(4):  
            now_cnt = cnt
            now_m = tree
            if dt ==1 or dt==3: 
                now_cnt += 1 # 회전을 위한 횟수 추가
            elif dt==2:
                now_cnt += 2
            now_cnt += 1 # 전진 이동횟수추가

            now_d = (d + dt)%4
            nr = r + dr[now_d]
            nc = c + dc[now_d]

            if is_valid(nr,nc):
                if arr[nr][nc] in ('G','Y') :
                    if visited[nr][nc][now_m] > now_cnt:
                        q.append((nr,nc, now_m , now_cnt, now_d))
                        visited[nr][nc][now_m] = now_cnt

                elif arr[nr][nc] == 'T' and now_m <m:
                    now_m += 1
                    if visited[nr][nc][now_m] > now_cnt:
                        q.append((nr,nc, now_m , now_cnt, now_d))
                        visited[nr][nc][now_m] = now_cnt

    if result == int(1e9):
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {result}')
        # 혹은 "Y"인곳의 visited 값중에 최솟값을 가져와도 됨

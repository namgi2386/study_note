import sys
sys.stdin = open('z2.txt' , 'r')

from collections import deque 

dr = [-1,0,1,0]
dc = [0,1,0,-1]
def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    m = int(input())
    result = [0]*(m)    # 여기에 결과저장
    command_arr=[input().split() for _ in range(m)]
    # [['7', 'RRAALAA'], ['8', 'RRAALAAA'], ['12', 'RAARRALAALAA']]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X':
                sr , sc = i,j

    for m_i in range(m):
        dir = 0             #방향초기화 
        r , c = sr , sc     #위치초기화
        num , st = command_arr[m_i]
        num = int(num)

        for ch in range(num):
            if st[ch] == 'R':
                dir = (dir + 1)%4
            elif st[ch] == 'L':
                dir = (dir + 3)%4
            elif st[ch] == 'A':
                nr = r + dr[dir]
                nc = c + dc[dir]
                if is_valid(nr,nc) and arr[nr][nc] != 'T':
                    r,c = nr,nc
        
        if arr[r][c] == 'Y':
            result[m_i] = 1
    
    print(f'#{tc} ', end="")
    print(*result)







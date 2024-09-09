# n번 구슬 (최대5회)
# w*h 배열 (최대 12*15 크기의 배열)
# 상하좌우 델타배열 + 가변길이
# 12열 중 하나선택 => 최대 5번 선택
# 순열 dfs로 완전탐색 해야할것같아

import sys
sys.stdin = open('z3.txt' , 'r')

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def shoot(lev , remains, nowarr):
    global min_blocks

    if lev==n or remains==0:
        min_blocks =  min(min_blocks , remains)
        return
    
    # 쏘기
    for col in range(w):
        # 1.
        # 원본 수정 후 복구 하지말고
        # 복사본 수정 => 다음재귀로 전달
        copy_arr = [i[:] for i in nowarr]
        row = -1
        for r in range(h):
            if copy_arr[r][col]:
                row = r
                break
        if row == -1:
            continue

        li=[(row,col , copy_arr[row][col])]
        now_remains = remains -1
        copy_arr[row][col] = 0

        while li:
            r,c,p = li.pop()
            for k in range(1,p):
                for i in range(4):
                    nr = r + dy[i]*k
                    nc = c + dx[i]*k

                    if n

        for c in range(w):
            idx = h-1

    # 변경된 배열

    # 중력 


for tc in range(1,int(input())+1):
    n , w,h = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(h)]
    
    min_blocks = 1e9
    blocks = 0              # 초기벽돌
    for i in arr:
        for j in i:
            if j:
                blocks += 1
    

    # 2.
    # 다 끝나고 남은벽돌 출력해야돼
    # 남아있는 벽돌이 없다면 끝낼거야
    # 현재 남은 벽돌 수 있으면 좋아

    # 3.
    # n번 시행
    # 시작은 0번 + 남은벽돌은 초기벽돌
    # n번 하면 끝 + 남은벽돌없으면 끝

    shoot(0, blocks , arr)
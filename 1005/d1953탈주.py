

dr = [-1,0,1,0]
dc = [0,1,0,-1]
# 0 상
# 1 우
# 2 하
# 3 좌

pipe = [[],[0,1,2,3],[0,2],[1,3],[0,1],[1,2],[2,3],[0,3]]
# pipe[i] == 방향인덱스

# for j in range(len(pipe[i]))

def is_correct(i , to_li):
    if i== 0  and 2 in to_li:
        return True
    if i== 1  and 3 in to_li:
        return True
    if i== 2  and 0 in to_li:
        return True
    if i== 3  and 1 in to_li:
        return True
    return False

def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<m

def where(lev):
    while True:
        lev += 1
        if not s:
            return
        r,c =s.pop(0) # 2,1
        idx = arr[r][c] # 3 값
        # last_nr = 0
        # last_nc = 0
        for i in pipe[idx]: # [1,3] 파이프 인덱스
            nr = r+dr[i]
            nc = c+dc[i]
            if is_valid(nr,nc) and arr[nr][nc] and not zero_arr[nr][nc] and is_correct(i ,pipe[arr[nr][nc]]) :
                s.append((nr,nc))
                if zero_arr[r][c] +1 == t+1:
                    return
                zero_arr[nr][nc] = zero_arr[r][c] +1
                # last_nr = nr
                # last_nc = nc
        # if tc==3:
        #     print('--'*10)
        #     for i in range(n):
        #         print(zero_arr[i])
        #     print('--'*10)
        # if zero_arr[last_nr][last_nc] == t:
        #     return




for tc in range(1,int(input())+1):
    n,m,pr,pc,t = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    zero_arr = [[0]*m for _ in range(n)]
    zero_arr[pr][pc] = 1
    s=[(pr,pc)]
    where(0)

    counts =0
    for i in range(n):
        for j in range(m):
            if zero_arr[i][j]:
                counts += 1
    # if tc==4:
    #     for i in range(n):
    #         print(arr[i])
    #     print('--'*10)
        # for i in range(n):
        #     print(zero_arr[i])
    print(f'#{tc} {counts}')

'''

5 6 2 2 6
3 0 0 0 0      3
q2 0 0 0 0     6
e1 w3 w w1 e3 q1
q2 0 w2 0  0   2
0 0 e4 q3  1   1

'''
import sys
sys.stdin = open('z2.txt' , 'r')

def is_valid(nr,nc):
    return 0<=nr<n and 0<= nc<n

def shutup_malfhoi(lev,s):
    global result , elec_result
    if lev == s_n:
        num , electronic = good(s)

        if electronic > elec_result:
            elec_result = electronic
            if num:
                result = min(result , num)
            return
    
    if sum(direction_list[lev]) ==0:
        s.append(5)
        shutup_malfhoi(lev+1 , s)
        s.pop()
    else:
        for i in range(4):
            if direction_list[lev][i] :
                s.append(i)
                shutup_malfhoi(lev+1 , s)
                s.pop()

def good(s):
    copy_arr = [row[:] for row in arr]
    counts = 0
    electronic = 0
    for i in range(s_n):
        if s[i] != 5:
            r,c = start_point[i]
            d = s[i]
            for k in range(1,n):
                nr = r +dr[d]*k
                nc = c +dc[d]*k
                if is_valid(nr,nc):
                    copy_arr[nr][nc] += 1
                    counts += 1
                    if copy_arr[nr][nc] >=2:
                        return 
            else :
                electronic += 1
    print(counts , electronic)
    return (counts , electronic)




dr = [-1,0,1,0]
dc = [0,1,0,-1]
# 0 상 1 우 2 하 3 좌

for tc in range(1,int(input())+1):
    n = int(input())
    arr =[list(map(int, input().split())) for _ in range(n)]
    result = 1e9
    elec_result = 0
    
    # 코어 최대 12개
    start_point =[]
    for i in range(1,n-1):
        for j in range(1,n-1):
            if arr[i][j] == 1:
                start_point.append((i,j))
    #시작점 리스트 완성
    s_n = len(start_point)

    
    direction_list = [[1,1,1,1] for _ in range(s_n)]

    for i in range(s_n):
        for d in range(4):
            for k in range(1,n):
                nr = start_point[i][0] + dr[d]*k
                nc = start_point[i][1] + dc[d]*k
                if is_valid(nr,nc) and arr[nr][nc]:
                    direction_list[i][d] = 0
    # [[0, 1, 1, 1], [1, 1, 1, 1], [1, 0, 0, 0], [1, 1, 1, 0], [0, 1, 1, 1]]
    temp_li = []
    # for i in range(s_n):
    #     for d in range(4):
    #         if direction_list[i][d]:
    #             nr,nc = start_point[i]
    #             # shutup_malfhoi(nr,nc,d)
    shutup_malfhoi(0,[])
    print(f'#{tc} {result}')





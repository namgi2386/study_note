import sys
sys.stdin = open('z2.txt' , 'r')
dr =[-1,1,0,0]
dc =[0,0,-1,1]
def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n

# 재귀단계 : 코어번호
# idx : 코어번호 , 현재 idx번째의 코어를 연결할지말지 고민중
# connected : 전원과 연결되어 있는 코어를 기억
# board : 현재 코어를 전선과 연결한 상태를 2차원 배열로 기억
# l : 현재까지 연결한 전선의 길이
def solve(idx , l , connected ,arr):
    global max_core_cnt , min_line_length

    if len(connected) + len(core_list) - idx < max_core_cnt:
        return


    if idx== len(core_list): # ??????????????? core_list +1
        if max_core_cnt < len(connected):
            max_core_cnt = len(connected)
            min_line_length = l
        elif max_core_cnt == len(connected):
            min_line_length = min(l, min_line_length)
        return
    r,c, = core_list[idx]
    if (r,c) in connected:
        solve(idx+1,l , connected , arr)
    else:
        for d in range(4):
            nr,nc = r,c
            temp_list =[]
            can_connect = True

            while True:
                nr += dr[d]
                nc += dc[d]
                if not is_valid(nr,nc):
                    break
                if arr[nr][nc] != 0:
                    can_connect = False
                    break
                temp_list.append((nr,nc))
            if can_connect:
                for (vr,vc) in temp_list:
                    arr[vr][vc] = 2
                solve(idx+1,l+len(temp_list) , connected + [(r,c)] , arr)

                for (vr,vc) in temp_list:
                    arr[vr][vc] = 0
    solve(idx+1,l,connected,arr)


resulr =[]
for tc in range(1,int(input())+1):
    n = int(input())
    arr =[list(map(int, input().split())) for _ in range(n)]
    max_core_cnt = 0
    min_line_length = n*n
    core_list =[] # 초기 코어 위치 기록
    connected_list =[] # 전류가 흐르는 코어 기록

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                core_list.append((i,j))
                if 1==0 or j==0 or i==n-1 or j==n-1:
                    connected_list.append((i,j))
    
    solve(0,0,connected_list,arr)
    resulr.append(f'#{tc} {min_line_length}')
print("\n".join(resulr))
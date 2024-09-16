from collections import deque

# 위 오른 아래 왼
dr = [-1,0,1,0]
dc = [0,1,0,-1]

def is_valid(nr,nc):
    return 1<=nr<n-1 and 1<= nc<n-1

def snake():
    d = 1 # 오른쪽 방향 시작
    q = deque()     # 몸이 위치하는 좌표들 기록
    q.append((1,1)) # 현재위치 1,1 에서 시작
    pr = 1 # 대가리 위치
    pc = 1 # 대가리 위치 기록
    date = 0


    while True:
        date += 1

        nr = pr + dr[d]
        nc = pc + dc[d]

        if is_valid(nr,nc) and (nr,nc) not in q: # 문제없을때
            if arr[pr][pc] == 1:            # 사과있으면
                q.append((nr,nc))
                arr[pr][pc] = 0
            else:                           # 사과 없다면
                q.append((nr,nc))
                q.popleft()
            pr , pc = nr , nc               # 대가리 위치 갱신
        else:                   # 벽만났거나 몸에박음
            # print(date , pr,pc,d)
            return date
        
        if dir_list and date == dir_list[0][0] :    # 방향전환해야한다면
            if dir_list[0][1] == 'L':
                d = (d+3)%4
            else:
                d = (d+1)%4
            dir_list.pop(0)


n = int(input()) +2         # 벽만들어줘야해서 +2 해줌
app_n = int(input())

arr = [[0]*(n) for _ in range(n) ]      # 여기에 사과 기록

for _ in range(app_n):
    a,b = map(int,input().split())
    arr[a][b] = 1                       # 사과를 1로 기록

dir_n = int(input())

# 숫자면 int로 받고 문자는 그대로 바꿈
dir_list = [list(map(lambda x: int(x) if x.isdigit() else x ,input().split())) for _ in range(dir_n)]


# 함수 실행
print(snake())
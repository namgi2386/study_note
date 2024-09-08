import sys
sys.stdin = open("z3.txt", "r")

# 2개 그룹으로 나누기
def combination(i, s1, s2):
    global min_time
    if i == len(people):
        s1_time = time_for_each_stair(stairs[0], s1) # 1번계단의 총 시간
        s2_time = time_for_each_stair(stairs[1], s2) # 2번계단의 총 시간

        total_time = max(s1_time, s2_time) # 2개의 계단 중 최대시간
        min_time = min(min_time, total_time) # 모든 경우의수에 대해 최소시간 갱신
        return

    combination(i + 1, s1 + [people[i]], s2) # 2개 그룹으로 나누기
    combination(i + 1, s1, s2 + [people[i]])

def time_for_each_stair(stair , peep):
    s_r , s_c , s_t = stair
    w_list = []

    for p_r , p_c in peep:
        distance = abs(p_r - s_r) + abs(p_c - s_c)
        w_list.append(distance)
    w_list.sort() 
    d_list = [] # downtown_remaining_time_list #[4,4,6] #내려가는3명 남은시간
    r_list = [] # ready_counts_list [0,0,0,0] 4명대기중
    time = 0

    while w_list or d_list or r_list:

        # 1. 내려가는 사람 시간줄이기
        if d_list:
            for i in range(len(d_list)-1,-1,-1):
                d_list[i] -= 1
                if d_list[i] ==0:
                    d_list.pop(i)
        
        # 2. 기다리는사람 내려가게 하기
        while r_list and len(d_list) < 3:
            d_list.append(s_t) # 계단내려가는시간값 추가
            r_list.pop(0)


        # 3. 도착안한사람 거리줄이고 0되면 기다리는 사람에 추가하기
        if w_list:
            for i in range(len(w_list)-1,-1,-1):
                w_list[i] -= 1
                if w_list[i]<=0:
                    # w_list.pop(0)
                    r_list.append(w_list.pop(i)) 

        # 4. 전체 시간 증가
        if w_list or d_list or r_list:
            time += 1
    return time


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    people = []
    stairs = []

    for r in range(n):
        for c in range(n):
            if arr[r][c] == 1: # 사람 추가
                people.append((r, c))
            elif arr[r][c] >= 2: # 계단추가
                stairs.append((r, c, arr[r][c])) # 좌표와 값추가

    min_time = 1e9
    combination(0, [], []) # 각각 1번 혹은 2번계단으로 이동
    print(f"#{tc} {min_time+1}")
import sys
sys.stdin = open("z3.txt", "r")

# 2개 그룹으로 나누기
def combination(i, s1, s2):
    global min_time
    if i == len(people):
        s1_time = calculate_stair_time(stairs[0], s1) # 1번계단의 총 시간
        s2_time = calculate_stair_time(stairs[1], s2) # 2번계단의 총 시간

        total_time = max(s1_time, s2_time) # 2개의 계단 중 최대시간
        min_time = min(min_time, total_time) # 모든 경우의수에 대해 최소시간 갱신
        return

    combination(i + 1, s1 + [people[i]], s2) # 2개 그룹으로 나누기
    combination(i + 1, s1, s2 + [people[i]])


def calculate_stair_time(stair, people_on_stair): #계단선택 , #입장인원 좌표 저장된 리스트
    stair_r, stair_c, stair_t = stair
    waiting_queue = [] # 사람부터 계단까지의 거리값들 넣을 리스트

    # 계단까지의 거리 계산
    for person_r, person_c in people_on_stair:
        distance = abs(person_r - stair_r) + abs(person_c - stair_c)
        # 계단 이용할 사람들 줄서서 기다리기
        waiting_queue.append(distance)

    # 거리가 가까운 순으로 정렬
    waiting_queue.sort()            # 계단으로 가는중

    # 계단 내려가는 사람들
    descending_queue = []           # 내려가는중

    # 계단 앞에 도착한 사람들
    ready_queue = []                # 기다리는중

    # 걸린 시간
    time = 0

    # 사람이 셋중에 하나라도 남아있으면 계속
    while waiting_queue or ready_queue or descending_queue:
        
        # 계단을 내려가는 중인 사람들 시간 -1
        descending_queue = [t - 1 for t in descending_queue if t - 1 > 0]

        # 계단에 도착한 사람들 처리
        while ready_queue and len(descending_queue) < 3:
            descending_queue.append(stair_t)  # 계단 내려가기 시작
            ready_queue.pop(0)

        # 계단에 도착하지 않은 사람들의 거리 -1
        i = 0
        while i < len(waiting_queue):
            if waiting_queue[i] == 0: # 계단에 도착하면 대기열에 추가
                ready_queue.append(waiting_queue.pop(i))  
            else:
                waiting_queue[i] -= 1
                i += 1  # 거리 감소 후 인덱스 증가

        # 아직 사람이 남아있으면 시간증가
        if waiting_queue or ready_queue or descending_queue:
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
    print(f"#{tc} {min_time}")

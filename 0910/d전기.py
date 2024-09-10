T = int(input())

for tc in range(1, T + 1):
    # 최소 몇 번 충전해야 종점 도착하는지 ?
    # 종점 도착 불가시 -> 0출력
    # 필요한 것 : 충전 회수 담을 그릇
    # K = 한번 충전 시 이동가능 거리, N = 총 길이, M = 충전기 설치된 정류장 개수
    K, N, M = map(int, input().split())
    # 전기 충전 위치
    lst = list(map(int, input().split()))
    # N + 1크기 만큼 배열 만들기
    arr = [0] * (N + 1)
    # 전기 충전 위치 배치해주기
    for i in lst:
        arr[i] = 1
    # 충전 회수
    charge_point = 0
    now_location = K
    while 1:

        if arr[now_location] == 1:
            charge_point += 1
            now_location += K
        else:
            now_location -= 1
            if now_location == K:
                break

        if now_location >= N:
            break

    print(F"#{tc} {charge_point}")
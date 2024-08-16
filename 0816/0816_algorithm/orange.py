# 3
# 4 B 2 O 1 O 2 B 4
# 3 B 5 B 8 O 100
# 2 O 2 O 1

T = int(input()) # 3
for tc in range(1, T + 1): # tc = 1
    data = input().split() # ['B', '2' ,'O', '1', 'O', '2', 'B', '4', ]
    N = int(data.pop(0)) # 4 # 버툰 뉴루눈 슈

    # 블루와 오렌지의 위치
    B, O = 1, 1  # 초기 위치는 각각 1
    # 버튼 누른시간
    bt, ot = 0, 0



    # 이전에 어떤 로봇이 버튼을 눌렀는지 표시 하기 위한 변수
    prev = data[0] # B


    # 실제로 버튼을 누르기
    for i in range(0,N*2,2): # 0 2 4 6
        robot = data[i] # B O O B
        btn = int(data[i+1]) # 2 1 2 4

        if prev == robot:   # 이전 버튼을 누른 로봇과 같은 로봇이 버튼을 누르는 상황 B B
            if robot == 'B':
                #블루로봇이 있는위치 B, 눌러야 하는 버튼 btn
                # 이동 시간 btn과 B의 차이 abs(btn - B)
                bt += abs(btn - B) + 1
                B = btn # 방금 버튼 누른 위치로 바꿔주기
            else:   #오렌지 로봇
                ot += abs(btn - O) + 1
                O = btn  # 방금 버튼 누른 위치로 바꿔주기

        else: # 다른 로봇이 버튼을 눌러야 되는 상황
            # 경우의 수를 좀 따져 봐야 합니다...
            # 다른 로봇이 버튼을 누르기 전에 이미 목적지에 도착한 상황
            # 도착하지 못한 상황
            if robot == 'B':
                # 오렌지가 버튼 누르기전에 이미 블루가 다음 버튼에 도착
                if bt + abs(btn - B) + 1<= ot:
                    # 오렌지가 버튼을 누를때 까지 기다려야 합니다.
                    bt = ot + 1
                else:
                    bt += abs(btn - B) + 1
                B = btn
            else: # 오렌지가 누를 차례
                if ot + abs(btn - O) + 1 <= bt:
                    # 오렌지가 버튼을 누를때 까지 기다려야 합니다.
                    ot = bt + 1
                else:
                    ot += abs(btn - O) + 1
                O = btn
        #다음 버튼을 누르러 가기전에... 이전 버튼 누른 로봇 변경해주기
        prev = robot
    result = max(ot, bt)
    print(f'#{tc} {result}')


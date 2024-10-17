from libs._bridge import init, submit, close


NICKNAME = "광주3반_정수연"
game_data = init(NICKNAME)


# 입력 데이터 분류
char_to_int = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
map_data = [[]]  # 맵 정보. 예) map_data[0][1] - [0, 1]의 지형/지물
allies = {}  # 아군 정보. 예) allies['A'] - 플레이어 본인의 정보
enemies = {}  # 적군 정보. 예) enemies['X'] - 적 포탑의 정보
codes = []  # 주어진 암호문. 예) codes[0] - 첫 번째 암호문

# 입력 데이터를 파싱하여 변수에 저장
def parse_data(game_data):
    # 입력 데이터를 행으로 나누기
    game_data_rows = game_data.split('\n')
    row_index = 0

    # 첫 번째 행 데이터 읽기
    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0])  # 맵의 세로 크기
    map_width = int(header[1])  # 맵의 가로 크기
    num_of_allies = int(header[2])  # 아군의 수
    num_of_enemies = int(header[3])  # 적군의 수
    num_of_codes = int(header[4])  # 암호문의 수
    row_index += 1

    # 기존의 맵 정보를 초기화하고 다시 읽어오기
    map_data.clear()
    map_data.extend([[ '' for c in range(map_width)] for r in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split(' ')
        for j in range(0, map_width):
            map_data[i][j] = col[j]
    row_index += map_height

    # 기존의 아군 정보를 초기화하고 다시 읽어오기
    allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        ally_name = ally.pop(0)
        allies[ally_name] = ally
    row_index += num_of_allies

    # 기존의 적군 정보를 초기화하고 다시 읽어오기
    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemy_name = enemy.pop(0)
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    # 기존의 암호문 정보를 초기화하고 다시 읽어오기
    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])

# 여기서부터 작성한 거
def bfs(map_data,start_x,start_y): # bfs로 최단거리 찾는 함수
    q = []
    q.append((start_x,start_y,0,[])) # 현재 위치의 좌표, 현재 방향, 가야하는 경로
    visited.add((start_x,start_y)) # 현재위치 방문체크

    while q:
        r,c,dir,path = q.pop(0)
        for d in range(4):
            nr,nc = r+dr[d],c+dc[d]
            # 유효한 인덱스이고 방문하지 않은 곳이면
            if 0<=nr<len(map_data) and 0<=nc<len(map_data[0]) and (nr,nc) not in visited:
                if map_data[nr][nc] == 'X': # 도착지점이면
                    return path + [(nr,nc,d)]
                elif map_data[nr][nc] == 'G' or map_data[nr][nc] == 'E1': # 풀
                    visited.add((nr,nc))
                    q.append((nr,nc,dir,path+[(nr,nc,d)]))

def solve(): # 암호 해독 함수
    new_code = ''
    for c in codes[0]:
        new_code += change[c]
    return new_code
# 여기까지

# while 반복문: 배틀싸피 메인 프로그램과 클라이언트(이 코드)가 데이터를 계속해서 주고받는 부분
while game_data is not None:
    # 자기 차례가 되어 받은 게임정보를 파싱
    print(f'----입력데이터----\n{game_data}\n----------------')
    parse_data(game_data)

    # 파싱한 데이터를 화면에 출력하여 확인
    print(f'\n[맵 정보] ({len(map_data)} x {len(map_data[0])})')
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            print(f'{map_data[i][j]} ', end='')
        print()

    print(f'\n[아군 정보] (아군 수: {len(allies)})')
    for k, v in allies.items():
        if k == 'A':
            print(f'A (내 탱크) - 체력: {v[0]}, 방향: {v[1]}, 보유한 일반 포탄: {v[2]}개, 보유한 대전차 포탄: {v[3]}개')
        elif k == 'H':
            print(f'H (아군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (아군 탱크) - 체력: {v[0]}')

    print(f'\n[적군 정보] (적군 수: {len(allies)})')
    for k, v in enemies.items():
        if k == 'X':
            print(f'H (적군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (적군 탱크) - 체력: {v[0]}')

    print(f'\n[암호문 정보] (암호문 수: {len(codes)})')
    for i in range(len(codes)):
        print(codes[i])


    # 탱크의 동작을 결정하기 위한 알고리즘을 구현하고 원하는 커맨드를 output 변수에 담기

    output = 'S'  # 알고리즘 결괏값이 없을 경우를 대비하여 초기값을 S로 설정

    my_position = [-1, -1] # 현재 내 위치
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if map_data[i][j] == 'A':
                my_position[0] = i
                my_position[1] = j
                break
        if my_position[0] > 0: break


# 여기서부터 또 작성한거
    # 암호문 해독 코드
    change = {'A':'J','B':'K','C':'L','D':'M','E':'N','F':'O','G':'P','H':'Q','I':'R','J':'S',
              'K':'T','L':'U','M':'V','N':'W','O':'X','P':'Y','Q':'Z','R':'A','S':'B','T':'C',
              'U':'D','V':'E','W':'F','X':'G','Y':'H','Z':'I'}
    #방향 상,하,좌,우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    visited = set() # 방문체크
    path_to_x = bfs(map_data,my_position[0],my_position[1])
    x,y = path_to_x[0][0],path_to_x[0][1] # 이동할 위치의 좌표
    point = path_to_x[0][2] # 이동할 위치의 방향
    # encode_cnt = 0
    if map_data[x][y] == 'X': # 이동할 곳이 도착지점이면
        popping = ['U F','D F','L F','R F']
        output = popping[point] # 이동할 방향에 맞는 공격명령 출력

    else: # 도착지점이 아니면
        if map_data[x][y] == 'G':  # 이동할 곳이 풀이면
            moving = ['U A', 'D A', 'L A', 'R A']
            output = moving[point]  # 이동할 방향에 맞는 이동명령 출력

        if int(allies['A'][3]) <= 5: # 갖고있는 포탄이 2개 이하이면
            for d in range(4): # 현재 지점 주위에 시설이 있다면
                nx,ny = my_position[0]+dr[d],my_position[1]+dc[d]
                if 0<=nx<len(map_data) and 0<=ny<len(map_data[0]) and (nx,ny) not in visited:
                    if map_data[nx][ny] == 'F': # 시설이면
                        visited.add((nx,ny)) # 시설 방문 처리
                        # 암호해독
                        result = solve()
                        output = 'G ' + result
                        print(allies['A'][3])

        # 포탄이 1개 이상 있고 적이 있으면
        if int(allies['A'][3]) >= 1 and map_data[x][y] in ('E1','E2','E3'):
            attack = ['U F S', 'D F S', 'L F S', 'R F S']
            output = attack[point]

# 여기까지


    # while 문의 끝에는 다음 코드가 필수로 존재하여야 함
    # output에 담긴 값은 submit 함수를 통해 배틀싸피 메인 프로그램에 전달
    game_data = submit(output)


# 반복문을 빠져나왔을 때 배틀싸피 메인 프로그램과의 연결을 완전히 해제하기 위해 close 함수 호출
close()
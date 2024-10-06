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


def bfs_shortest_path(map_data, sr, sc):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    n = len(map_data)
    m = len(map_data[0])
    q = []
    q.append(( sr, sc, [] ))
    visited = [[0]*m for _ in range(n)]
    visited[sr][sc] = 1
    
    while q:
        r, c,  path = q.pop(0)
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if 0 <= nr < len(map_data) and 0 <= nc < len(map_data[0]) and not visited[nr][nc]:
                if map_data[nr][nc] == "X":
                    return path + [(nr, nc, d)]
                elif map_data[nr][nc] == 'G'or map_data[nr][nc] == 'E1':
                    visited[nr][nc] = 1
                    q.append((nr, nc, path + [(nr, nc, d)]))
    return None

# 파일에서 입력 값을 불러와서 game_data에 저장하는 부분
with open('input.txt', 'r') as f:
    game_data = f.read()


rocket = False
while game_data:
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

    print(f'\n[적군 정보] (적군 수: {len(enemies)})')
    for k, v in enemies.items():
        if k == 'X':
            print(f'H (적군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (적군 탱크) - 체력: {v[0]}')

    print(f'\n[암호문 정보] (암호문 수: {len(codes)})')
    for i in range(len(codes)):
        print(codes[i])




    output = 'S'  
    # 시작점 찾기
    sr, sc = -1, -1
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if map_data[i][j] == 'A':
                sr, sc = i, j
                break
        if sr != -1:
            break

    hea_eng = {
    'A' : 'T', 'B' : 'U', 'C' : 'V', 'D' : 'W', 'E' : 'X', 'F' : 'Y', 'G' : 'Z',
    'H' : 'A', 'I' : 'B', 'J' : 'C', 'K' : 'D', 'L' : 'E', 'M' : 'F', 'N' : 'G',
    'O' : 'H', 'P' : 'I', 'Q' : 'J', 'R' : 'K', 'S' : 'L', 'T' : 'M', 'U' : 'N',
    'V' : 'O', 'W' : 'P', 'X' : 'Q', 'Y' : 'R', 'Z' : 'S'
    }
    # BFS로 최단 경로 찾기
    

    if not codes or rocket:
        path_to_x = bfs_shortest_path(map_data, sr, sc)
        go_r = path_to_x[0][0]
        go_c = path_to_x[0][1]
        point = path_to_x[0][2]
        if map_data[go_r][go_c] == 'X': # 도착일때 공격
            attack_li = [  'U F' ,'D F', 'L F' , 'R F' ]
            output = attack_li[point]
        else: 
            run_li = [ 'U A' , 'D A' , 'L A', 'R A'   ]
            output = run_li[point]
    elif not rocket:
        hea_result ="G "
        for st in codes[0]:
            hea_result += hea_eng[st]
        output = ""
        output += hea_result


    print("---output---")
    print(output)
    print("---output---")
    game_data = ""
    # game_data = submit(output)

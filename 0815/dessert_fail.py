import sys
sys.stdin = open('z3.txt' , 'r')

def make_way_list(n):
    way_list =[]
    for i in range(1,n):
        for j in range(1,n):
            way_list.append((i,j))
    return way_list

def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n

def classification_way(way_list):
    way_n =len(way_list) 
    
    way_valid = []

    for i in range(n):
        for j in range(n):
            for w in range(way_n):
                rd = way_list[w][0] # 오른쪽 아래로 이동할 수 있는 칸 수
                ld = way_list[w][1] # 왼쪽 아래로 이동할 수 있는 칸 수

                nr = i + rd   #(i,j)여기>#  1번
                nc = j + rd            #   #
                               #2번  #   #
                nrr = i + ld       #   #  4번    
                ncc = j - ld    #3번 #
                if is_valid(nr,nc) and is_valid(nrr,ncc): # 1번() 2번 확인
                    nr += ld 
                    nc -= ld

                    nrr += rd
                    ncc += rd # 사실 nr== nrr , nc==ncc
                    if is_valid(nr,nc) and is_valid(nrr,ncc): # 3번4번 확인
                        way_valid.append((i,j,way_list[w]))
    return way_valid # [(0, 1, (1, 1)), (0, 1, (2, 1)), (0, 2, (1, 1)), (0, 2, (1, 2)), (1, 1, (1, 1)), (1, 2, (1, 1))]

dr = [1,1,-1,-1]
dc = [1,-1,-1,1] # 5시 7시 11시 1시 순서

def last_way_check(way_valid):
    
    maximim_counts = -1
    for wtc in range(len(way_valid)):
        r,c,w = way_valid[wtc]
        w1 = w[0] # 우하단 이동거리 (출발)
        w2 = w[1] # 좌하단 이동거리
        w3 = w[0] # 우상단 이동거리
        w4 = w[1] # 우상단 이동거리 (도착)
        counts = [matrix[r][c]]
        for _ in range(1,w1+1):
            nr = r+dr[0]
            nc = c+dc[0]
            counts.append(matrix[nr][nc])
        for _ in range(1,w2+1):
            nr += dr[1]
            nc += dc[1]
            counts.append(matrix[nr][nc])
        for _ in range(1,w3+1):
            nr += dr[2]
            nc += dc[2]
            counts.append(matrix[nr][nc])
        for _ in range(1,w4): # 범위 주의
            nr += dr[3]
            nc += dc[3]
            counts.append(matrix[nr][nc])
        if len(counts) == len(set(counts)):

            if len(counts) > maximim_counts:
                maximim_counts = len(counts)

    return maximim_counts


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    way_list = make_way_list(n)
    way_valid = classification_way(way_list)
    result = last_way_check(way_valid)
    print(f'#{tc} {result}')



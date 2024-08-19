import sys
sys.stdin = open('z3.txt','r')

import copy
# 전체순회 사각형찾기 왼쪽위 꼭짓점 만났을때 아래로 이동후 오른쪽이동하여 오른아래꼭짓점 찾음
# square 리스트에 저장함 각각 4개의 꼭짓점 튜플 형태로 제작 (왼위 왼아래 오른아래 오른위 ) 순서

def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n

def square(arr):
    little_square_list =[]
    for i in range(n):
        for j in range(n):
            hi = 1
            hj = 1

            if arr[i][j] :
                little_square_position = [(i,j)]
                while is_valid(i+hi,j) and arr[i+hi][j]:
                    hi+=1
                hi-=1
                little_square_position.append((i+hi,j))
                while is_valid(i+hi,j+hj) and arr[i+hi][j+hj]:
                    hj += 1
                hj -= 1
                little_square_position.append((i + hi, j+hj))
                little_square_position.append((i, j+hj))
                little_square_list.append(little_square_position)

                for hk in range(i, i+hi+1):
                    for hl in range(j, j+hj+1):
                        arr[hk][hl] = 0

                # if hi==0:
                #     hhi = 0
                #     while is_valid(i,j+hhi) and arr[i][j+hhi] :
                #         print(333)
                #         arr[i][j+hhi] = 0
                #         hhi += 1
                #
                # elif hj==0:
                #     hhj = 0
                #     while is_valid(i+hhj,j) and arr[i+hhj][j] :
                #         print(444)
                #         arr[i+hhj][j] = 0
                #         hhj += 1

                # print()
                # print(i,j,hi,hj,arr)

    return little_square_list
# [[(0, 0), (1, 0), (1, 1), (0, 1)], [(0, 4), (4, 4), (4, 4), (0, 4)], [(4, 0), (4, 0), (4, 1), (4, 1)]]




# square리스트의 각변으로부터 가장가까운 지점 컨택
    # 컨택이 불가하다면 -1출력
# ( 시작지점 , 끝지점 , 거리 ) 튜플로 저장
def dista(square_list):
    sqn = len(square_list)
    dista_list=[]
    for i in range(sqn):
        for i1 in range(square_list[i][0][0] , square_list[i][1][0]+1): # 서쪽전진
            h=1
            while is_valid(i1,square_list[i][0][1]-h ):

                if backup_arr[i1][square_list[i][0][1]-h] :

                    for sqi in range(sqn):
                        if sqi != i:
                            #print(i, i1, square_list[i][0][1] - h , square_list[sqi][3][1])
                            if square_list[i][0][1]-h == square_list[sqi][3][1] and  square_list[sqi][3][0] <= i1 <= square_list[sqi][2][0]:
                                dista_list.append( (sqi , i , h-1) )
                h +=1
    
    for i in range(sqn):
        for i1 in range(square_list[i][1][1] , square_list[i][2][1]+1): # 남쪽전진
            h=1
            while is_valid(square_list[i][1][0]+h , i1): # (square_list[i][1][0]+h , i1)
                if backup_arr[square_list[i][1][0]+h][i1] :
                    for sqi in range(sqn):
                        if sqi != i:
                            #print(i, i1, square_list[i][0][1] - h , square_list[sqi][3][1])
                            if square_list[i][1][0]+h == square_list[sqi][0][0] and square_list[sqi][0][1] <= i1 <= square_list[sqi][3][1]:
                                dista_list.append( (sqi , i , h-1) )
                h +=1
    # [[(0, 0), (1, 0), (1, 1), (0, 1)], [(0, 4), (4, 4), (4, 4), (0, 4)], [(4, 0), (4, 0), (4, 1), (4, 1)]]
    
    
    return list(set(dista_list))

#####################
# [     1     ]


# [2] [3]   [4]
#####################

def get_shortcut():
    global s
    global result
    nn = len(distance_list)
    sn = len(square_list)

    if len(s) == sn-1:
        dc_list =[]
        for dc in range(sn-1):
            if (s[dc][0] ,s[dc][1]) not in dc_list and (s[dc][1] ,s[dc][0]) not in dc_list:
                dc_list.append( (s[dc][0] ,s[dc][1]) )

        if len(dc_list) == sn-1:
            sc_result = 0
            for sc in range(sn-1):
                sc_result += s[sc][2]
                print(sc_result)
                result = min(sc_result,result)
        return
    
    for i in range(nn): #1 [(0, 1, 2), (2, 1, 1), (2, 0, 2)]
        di = distance_list[i]
        if di not in s:
            s.append(di)
            #print(f'{i} {di} {s}')
            get_shortcut()
            s.pop()
            #print(f'{i} {di} {s}')

# 123 133 143 231 342 > 선택지 중에서 (n-1)개뽑기
        # n 개의 섬 n-1개의 다리보다 많거나 적을수 있나? 없다.
# 뽑힌 선택지의 ( a b d ) 값중
# a , b 값들을 전부 모음
# set 로 중복제거
# 제거된 set의 길이가 섬의 갯수와 동일할 때
# 그때 뽑힌선택지의 d 거리값의 합 계산 후 최솟값 출력





T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n) ]
    backup_arr = copy.deepcopy(arr)
    square_list = square(arr)
    distance_list = dista(square_list)

    s = []
    result = n*n
    get_shortcut()
    




    #print(f'#{tc} {distance_list}')
    print(result)
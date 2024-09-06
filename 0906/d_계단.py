import sys
sys.stdin = open('z3.txt' , 'r')





for tc in range(int(input())):
    n = int( input())
    arr = [ list(map(int, input().split())) for _ in range(n)]
    person_arr = []
    stair_arr = []
    for i in range(n):
        for j in range(n):
            if not arr[i][j]:
                pass
            elif arr[i][j]==1: 
                person_arr.append([i,j,0,0])
            else:
                stair_arr.append((i,j,arr[i][j]))
    p_n = len(person_arr)
    for i in range(2):
        for j in range(p_n):
            dx = abs(stair_arr[i][0] - person_arr[j][0])
            dy = abs(stair_arr[i][1] - person_arr[j][1])
            person_arr[j][i+2] = dx+dy
    # print(person_arr) # 좌표 , 1번출구거리 , 2번출구거리
    # print(stair_arr) # 좌표 , 값
    for dec in range(1<<p_n):
        stair_no1 =[0]*50
        stair_no2 =[0]*50
        for i in range(p_n):
            if dec & (1<<i):
                pet = person_arr[i][2]
                tt = 0
                while True:
                    if stair_no1[pet+tt] < 3:
                        for j in range(stair_arr[0][2]):
                            stair_no1[pet+j] += 1
                        break
                    else:
                        tt += 1
            else:
                pet = person_arr[i][3]
                tt = 0
                while True:
                    if sum(stair_no2[pet+tt:pet+tt+stair_arr[i][2]]) < 3*stair_arr[i][2]:
                        for j in range(stair_arr[1][2]):
                            stair_no2[pet+j] += 1
                        break
                    else:
                        tt+=1
        print(stair_no1)
        print(stair_no2)
    if tc==1:
        print(person_arr)
        print(stair_arr)
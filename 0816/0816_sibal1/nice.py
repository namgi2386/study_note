import sys
sys.stdin = open('z2.txt','r')

def is_linked(magnatic):
    m1 = magnatic[0]
    m2 = magnatic[1]
    m3 = magnatic[2]
    m4 = magnatic[3]
    linked = [0] * 3
    if m1[2] != m2[6]:
        linked[0] = 1
    else:
        linked[0] = 0
    if m2[3] != m3[6]:
        linked[1] = 1
    else:
        linked[1] = 0
    if m3[3] != m4[6]:
        linked[2] = 1
    else:
        linked[2] = 0
    return linked # [1,0,1]

def rolling(magnatic , my):



T = int(input())
for tc in range(1,T+1):
    n = int(input())
    magnatic = [list(map(int,input().split())) for _ in range(4)]

    arr = [list(map(int,input().split())) for _ in range(n)]
    m1 = magnatic[0]
    m2 = magnatic[1]
    m3 = magnatic[2]
    m4 = magnatic[3]

    for i in range(n):
        my_mag = arr[i][0]
        lol = arr[i][1]

        linked = is_linked(magnatic)
        if linked[0] ==1:




    # point_arr = [m1[0],m2[0],m3[0],m4[0]]
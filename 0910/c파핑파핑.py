import sys
sys.stdin = open('z2.txt','r')

from collections import deque

dr =[-1,1,0,0,-1,-1,1,1]
dc =[0,0,1,-1,-1,1,-1,1]
def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n

for tc in range(1,int(input())+1):
    n = int(input())
    arr =[list(input()) for _ in range(n)]

    num_arr = [ [0]*n for _ in range(n) ] # 90000

    for i in range(n):
        for j in range(n):
            position_cnt = 0
            if arr[i][j] =='.':
                for d in range(8):
                    nr = i + dr[d]
                    nc = j + dc[d]
                    if is_valid(nr,nc) and arr[nr][nc]=='*':
                        position_cnt += 1
                num_arr[i][j] = position_cnt
            else:
                num_arr[i][j] = '*'

    cnt = 0
    for i in range(n):
        for j in range(n):
            q=deque()
            if not num_arr[i][j]:
                q.append((i,j))
                num_arr[i][j] = 1
                while q:
                    r,c = q.popleft()
                    for d in range(8):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if is_valid(nr,nc):
                            temp = num_arr[nr][nc]
                            if temp == 0:
                                q.append((nr,nc))
                                arr[nr][nc] = 1
                                num_arr[nr][nc] = '*'

                            elif temp != '*':
                                arr[nr][nc] = 2

    if tc==1:
        for i in range(n):
            print(arr[i])
        print()
        for i in range(n):
            print(num_arr[i])


    for i in range(n):
        for j in range(n):
            pass


'''
..*..
..*..
.*..*
.*...
.*...

02*20
13*31
2*22*
3*311
2*200

02*20
13*31
2*22*
3*311
2*200
'''

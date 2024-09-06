import sys
sys.stdin = open('z1.txt' , 'r')


def back_mountain(i,j,lev):
    global back_result
    this_position = arr[i][j]
    for d in range(4):
        nr = i + dr[d]
        nc = j + dc[d]
        if is_valid(nr,nc) and this_position < arr[nr][nc] :
            back_mountain(nr,nc,lev+1)
    else:
        back_result = max(back_result , lev)



def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n

dr =[-1,0,1,0]
dc =[0,1,0,-1]

for tc in range(1,int(input())+1):
    n,dick = map(int , input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    back_result = 0
    for i in range(n):
        for j in range(n):
            back_mountain(i,j,1)

    for fuck in range(1,dick+1):
        for i in range(n):
            for j in range(n):
                po_arr = []
                po_s=[]
                for d in range(4):
                    nr = i + dr[d]
                    nc = j + dc[d]
                    if is_valid(nr,nc) and arr[nr][nc] < arr[i][j]:
                        po_arr.append((nr,nc))
                    if is_valid(nr,nc) and arr[nr][nc] < arr[i][j]:





def inner(t):
    if len(po_s)==2:
        total_li.append(po_s[:])
        return
    for i in range(t,n//2):
        if i not in po_s:
            po_s.append(i)
            inner(i)
            po_s.pop()



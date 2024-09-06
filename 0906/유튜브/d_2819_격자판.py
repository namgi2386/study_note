import sys
sys.stdin = open('z4.txt' , 'r')

def is_valid(nr,nc):
    return 0<=nr<4 and 0<=nc<4

dr =[-1,0,1,0]
dc =[0,1,0,-1]

def warm(i,j,my_str):
    if len(my_str)==7:
        result.add(my_str)
        return
    
    for d in range(4):
        nr = i + dr[d]
        nc = j + dc[d]
        if is_valid(nr,nc):
            warm(nr,nc,my_str+arr[nr][nc])



for tc in range(1,int(input())+1):
    arr = [input().split() for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
                warm(i,j,arr[i][j])
    print(f'#{tc} {len(result)}')
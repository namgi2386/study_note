import sys
sys.stdin = open('z1.txt' , 'r')


def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n

dr =[-1,0,1,0]
dc =[0,1,0,-1]

for tc in range(1,int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    maxium_position = [0]*(n**2+1)

    for i in range(n):
        for j in range(n):
            for d in range(4):
                nr = i+ dr[d]
                nc = j + dc[d]
                if is_valid(nr,nc) and arr[nr][nc] == arr[i][j] +1 :
                    maxium_position[arr[i][j]] = 1
    counts = 1
    result = 0
    result_idx = 0
    for i in range(n*n,-1,-1):
        if maxium_position[i]:
            counts +=1
            if counts >= result:
                result = counts
                result_idx = i
        else:
            counts =1
    print(f'#{tc} {result_idx} {result}')
# 제한시간 : 4초 ==>> 1억2천
# 27개 tc ========>> 하나의 tc당 (최대444만번)
# n^2 100만
# 모든칸에 상하좌우 4칸확인 ==> 그대로 하게되면 뭔가 빡빡할듯!
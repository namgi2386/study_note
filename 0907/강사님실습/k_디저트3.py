# 34분
# import sys
# sys.stdin = open("z4.txt", "r")

dr = [1,1,-1,-1]
dc = [-1,1,1,-1]

def my_flower():
    # 최대길이 total_lenth 2~ n-1까지 까지 가능?
    for total_lenth in range(n-1,1,-1):
        # 좌하단 길이
        for left in range(1,total_lenth):
            right = total_lenth - left

            for r in range(n-total_lenth):
                for c in range(left,n-right):
                    # nr , nc 탐색의 시작지점
                    visited = [0]*101
                    nr , nc = r,c
                    for d in range(4):
                        if not d%2 :
                            l = left
                        else:
                            l = right
                        

                        # print(total_lenth ,left,right, n, nr,nc)
                        for _ in range(l):
                            nr += dr[d]
                            nc += dc[d]
                            if visited[arr[nr][nc]] ==0:
                                visited[arr[nr][nc]] = 1
                            else:
                                break
                        else:
                            continue
                        break
                    else:
                        return total_lenth*2
    return -1





for tc in range(1,int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{tc} {my_flower()}')


#19분
import sys
sys.stdin = open('z1.txt' , 'r')

def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n

def solve(nr,nc,nk): # center position , nk=3 => 5*5
    counts =0
    for i in range(-(nk-1),nk): #row -2 -1 0 1 2
        itoj = (nk-1)-abs(i) # 0 , 1 , 2
        for j in range( -itoj,itoj+1 ): # col 00 , -1 1 , -2,2
            # print(nr,nc,i,j)
            if arr[nr + i][nc + j]==1:
                counts += 1
    return counts


for tc in range(1, int(input())+1):
    n , m = map(int, input().split())
    arr =[list(map(int,input().split())) for _ in range(n)]
    
    k = (n+1)//2
    result = 0
    debug_cnt = 0
    for nk in range(1,k): # 최대 방범 
        for r in range(n):
            for c in range(n):
                if is_valid(r-nk+1 , c-nk+1) and is_valid(r+nk-1 , c+nk-1):
                    house_cnt = solve(r,c,nk)
                    paid = nk**2 +(nk-1)**2
                    income = paid - house_cnt*m
                    if income > result:
                        result = income
                        debug_cnt = house_cnt

    print(f'#{tc} {debug_cnt} {result}')





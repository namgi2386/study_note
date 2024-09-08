def is_valid(nr,nc):
    return 0<=nr<n and 0<=nc<n

def home():
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            for k in range(1, n+2): # k = 1~ (2*n-1)
                cover_counts = k*k + (k-1)*(k-1) # k=3 일때 , 13
                home_counts = 0
                for hi in range(-(k-1),(k-1)+1): # k=3일때, [-2,-1,0,1,2]
                    tt = (k-1)-abs(hi) # 0 1 2 1 0
                    for hj in range(-tt , tt +1 ):
                        nr = i +hi
                        nc = j +hj
                        if is_valid(nr,nc) and arr[nr][nc] :
                            home_counts += 1
                profit = home_counts*m - cover_counts
                if profit >=0:
                    result = max( result , home_counts)
    return result




T = int(input())
for tc in range(1,T+1):

    n,m = map(int,input().split())
    result = home()
    print(f'#{tc} {result}')
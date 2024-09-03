
for tc in range(1,int(input())+1):
    n = int(input())
    arr =[ list(map(int,input().split())) for _ in range(n) ] 
    arr.sort(key=lambda x:x[1])
    
    start_idx = 0
    counts =0
    for i in range(n):
        if arr[i][0] >= start_idx:
            counts += 1
            start_idx = arr[i][1]
    print(f'#{tc} {counts}')
    print("ㅎㅇ")
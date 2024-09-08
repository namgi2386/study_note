def find(n, k, p, m, sumX, sumY):
    global minV
    if(p==N//2 and m==N//2):
        dis = sumX*sumX + sumY*sumY
        if(minV>dis):
            minV = dis
    else:
        if(p<(N//2)):
            find(n+1, k, p+1, m, sumX+pos[n][0], sumY+pos[n][1]) # 벡터 계산에서 절반은 +, 절반은 -로 구성됨
        if(m<(N//2)):
            find(n+1, k, p, m+1, sumX-pos[n][0], sumY-pos[n][1])
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pos = [0]*N
    for i in range(N):
        pos[i]= list(map(int, input().split()))
    minV = 1000000000000
    find(1, N, 1, 0, pos[0][0], pos[0][1])
    print('#{} {}'.format(tc, minV))
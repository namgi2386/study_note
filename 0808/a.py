T = int(input())
 
for tc in range(1,T+1):
    A, B = input().split()
 
    str_cnt = 0
 
    Al = len(A)
    Bl = len(B)
 
    Ai = 0
    Bi = 0
 
    while Ai < Al:
        if A[Ai] != B[Bi]:
            Ai += 1
            if Bi !=0:
                Bi = 0
        else:
            Ai +=1
            Bi +=1
            if Bi == (Bl):
                str_cnt += 1
                Bi = 0
                Ai += 1
    print(f'#{tc} {Al-(Bl*str_cnt)+str_cnt}')
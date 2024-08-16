for tc in range(1,int(input())+1 ):
    n = int(input())
    arr =[list(map(int,input().split())) for _ in range(n)]
    # for _ in range(n):
    #   a,b = map(int,input().split() ) <<< 이거도 가능 (어짜피 2개씩 입력됨)
    
    b = [0]*5001
    for i in range(n):
        for j in range(arr[i][0],arr[i][1]+1):
            b[j] += 1
    
    print(f'#{tc} ',end="")
    p = int(input())
    for i in range(p):
        print(f'{b[int(input())]}', end=" ")
    print()
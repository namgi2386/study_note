import sys
sys.stdin = open('z2.txt','r')

T = int(input())
for tc in range(1,T+1):
    n , m = map(int,input().split())
    matrix = [input() for _ in range(n)]
    result = 0
    for x in matrix[0]:
        if x != 'W':
            result += 1
    for x in matrix[-1]:
        if x != 'R':
            result += 1
    center_matrix = matrix[1:-1]
    count_matrix = [[0]*3 for _ in range(n-2)]
    for i in range(n-2):
        for j in range(m):
            if center_matrix[i][j] == 'W':
                count_matrix[i][0] += 1
            if center_matrix[i][j] == 'B':
                count_matrix[i][1] += 1
            if center_matrix[i][j] == 'R':
                count_matrix[i][2] += 1

    center_arr = []
    for w in range(0,n-2): # 총 n=7칸이며 , 가운데 n-2=5칸이라고하면 w 는 0~4칸
        for t in range(1,n-1-w): # w부터 끝까지 가능해야함 
            for r in range(n-2-w-t,n-1-w-t): # w+t부터 끝까지
                center_arr.append([w,t,r])
    
    for s in range(len(center_arr)):
        w , b , r = center_arr[s][0] , center_arr[s][1] , center_arr[s][2]
        for ww in range(w+1):
            for bb in range(ww,ww+b+1):
                for rr in range(ww+bb,n-1):
                    






    # 행의 인덱스 범위 지정
    # for w in range(0,n-2): # 총 n=7칸이며 , 가운데 n-2=5칸이라고하면 w 는 0~4칸
    #     for t in range(w,n-1): # w부터 끝까지 가능해야함 
    #         for r in range(w+t,n-1): # w+t부터 끝까지

            # r = n-2 -w -t  # r은 나머지 할당

            
    #     for i in range(0,h):
    #         set_result += m - count_matrix[i][0]
    #     for i in range(0,)
        
    #         for j in range(1,n-2-i):
    #             k = n-2-i-j 
    #             temp += m - count_matrix[i][0]
    #             temp += m - count_matrix[j][1]
    #             temp += m - count_matrix[k][2]
    # print(f'#{tc} {set_result + temp}')

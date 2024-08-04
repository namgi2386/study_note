import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    li = list(map(int,input().split()))
    n = li[0]
    w = li[1]
    matrix = []
    for _ in range(n): 
        matrix.append(list(map(int,input().split())))

    result = 0

    for i in range(n):
        for j in range(n):
            count_r1,count_r2 = 0,0
            count_c1,count_c2 = 0,0
            if matrix[i][j] :
                if j+w-1 < n:
                    for h in range(1,w):
                        if j==0 and matrix[i][j+h]==1 :
                            if j+w==n or matrix[i][j+w]==0 :
                                
                                count_r1 += 1
                    if count_r1 == w-1:
                        #print(f"#{tc}_r1 : on + {i+1}행,{j+1}열 ")
                        result += 1
                    
                    for h in range(1,w):
                        if j != 0 and matrix[i][j-1]==0 and matrix[i][j+h]==1 :
                            if j+w==n or matrix[i][j+w]==0 :
                                
                                count_r2 += 1
                    if count_r2 == w-1:
                        #print(f"#{tc}_r2 : on + {i+1}행,{j+1}열 ")
                        result += 1
                
                if i+w-1 < n: # i=0 j=3 w=3 n=5 k=1,2
                    for k in range(1,w):
                        if i==0 and matrix[i+k][j]==1:
                            if i+w==n or matrix[i+w][j]==0:
                                count_c1 += 1
                    if count_c1 == w-1:
                        #print(f"#{tc}_c1 : on + {i+1}행,{j+1}열 ")
                        result += 1

                    for k in range(1,w):
                        if i != 0 and matrix[i-1][j]==0 and matrix[i+k][j]==1:
                            if i+w==n or matrix[i+w][j]==0:
                                count_c2 += 1
                    if count_c2 == w-1:
                        #print(f"#{tc}_c2 : on + {i+1}행,{j+1}열 ")
                        result += 1
    print(f"#{tc} {result}")
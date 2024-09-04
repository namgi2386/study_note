import sys
sys.stdin = open('z1.txt' , 'r')
def f():
    global min_num
    while True:
        if sum(step) >= m :
            return
        for i in range(n):
            k = 1
            while arr[i]//(step[i]+k) >= min_num :
                step_arr[i].append(arr[i]//(step[i]+k))
                step_arr[i][step[i]]
                k += 1
            step[i] += k
            step_arr[i].append(arr[i]//(step[i]+k+1))
        
        min_num = arr[0]//(step[0]+1)
        temp_step = 0
        for i in range(n):
            print(step_arr , step)
            my_num = step_arr[i][step[i]]
            if my_num> min_num:
                min_num = my_num
                temp_step = i
        step[temp_step] += 1



for tc in range(1,int(input())+1):
    n , m = map(int,input().split()) # n=4 , m=10

    arr = list(map(int,input().split())) # [6894, 3441, 4999, 2771]
    min_num = min(arr)

    step_arr = [[] for _ in range(n)]
    for i in range(n):
        step_arr[i].append(arr[i]) # [[6894], [3441], [4999], [2771]]
    
    step = [0]*n # 단 이렇게 하면 모든종류의 사탕을 하나씩은 넣어야함
    
    

    if sum(arr) >= m:
        f()
        min_num = arr[0]
        for i in range(n):
            if step[i] != 1:
                min_num = min(arr[i]//(step[i]-1) , min_num)
            else:
                min_num = min(arr[i] , min_num)
        print(f'#{tc} {min_num}')
    else:
        min_num = 0
        print(f'#{tc} {min_num}')


    

# [2771] (4999 3441) 6894 # 위에 4개 선택
#  1385  2499 1720  (3447) 갱신  > step1 실패 
#                    2294
# step = 2 1 1 1 갱신됨


# 4
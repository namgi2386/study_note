T = int(input())
switch_arr = list(map(int , input().split() ))
switch_arr.insert(0,'s') # 인덱스번호와 스위치번호 맞추기

n = int(input())
user_arr = [list(map(int , input().split() )) for _ in range(n)]

for i in range(n):
    if user_arr[i][0] == 1: # 남학생일때
        switch_idx = user_arr[i][1] # i번째 학생이 조작할 스위치 번호
        temp_idx = switch_idx
        while temp_idx < T+1:
            switch_arr[temp_idx] = abs(switch_arr[temp_idx] -1) # 0,1교환
            temp_idx += switch_idx # 배수 늘려주기

    else : # 여학생일때
        switch_idx = user_arr[i][1]
        switch_arr[switch_idx] = abs(switch_arr[switch_idx] -1)
        jump = 1
        while switch_idx + jump < T+1  and switch_idx - jump > 0 :
            if switch_arr[switch_idx+jump] == switch_arr[switch_idx-jump]:
                switch_arr[switch_idx+jump] = abs(switch_arr[switch_idx+jump] -1)
                switch_arr[switch_idx-jump] = abs(switch_arr[switch_idx-jump] -1)
                jump += 1
            else :
                break


result = switch_arr[1:]
for idx in range(len(result)):
    print(result[idx], end=" ")
    if (idx+1)%20 ==0:
        print()

from collections import deque

def f():
    while q:
        num , cnt = q.popleft()
        if num==1:
            continue
        next_cnt = cnt+ 1
        for idx in range(2,4):
            if num%idx==0:
                next_num = num//idx
                if cnt_arr[next_num] > next_cnt:
                    cnt_arr[next_num] = next_cnt
                    q.append((next_num,next_cnt))
        
        next_num = num -1
        if cnt_arr[next_num] > next_cnt:
            cnt_arr[next_num] = next_cnt
            q.append((next_num,next_cnt))



start_num = int(input())
cnt_arr = [1e9]*(start_num+1)
q = deque()
q.append((start_num,0))
cnt_arr[start_num] = 0
f()
print(cnt_arr[1])
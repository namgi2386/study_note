import sys
sys.stdin = open('z1.txt' , 'r')

T = int(input())
for tc in range(1,T+1):
    set_arr = list(input().split())
    n = int(set_arr[0])
    arr = set_arr[1:]

    plag = 'ready'
    turn = 0
    total_turn = 0
    b_position = 1
    o_position = 1
    for i in range(n):
        num = int(arr[2*i+1]) # 해당위치의 숫자
        
        if plag == 'ready': # 첫값 초기작업
            if arr[2*i] == 'B':
                plag = 'B'
                b_position = num
                turn += num
                total_turn += turn
                #print(f'num: {num} , turn: {turn} , t : {total_turn} , plag : {plag}')
                continue
            else :
                plag = 'O'
                o_position = num
                turn += num
                total_turn += turn
                continue

        if arr[2*i] == 'B' and plag == 'B': # 일치
            b_position = num
            turn += abs(num - int(arr[2*(i-1)+1])) +1 
            total_turn += abs(num - int(arr[2*(i-1)+1])) +1 
        elif arr[2*i] == 'B' and plag != 'B':
            if num <= turn + 1:
                turn = 1
                b_position = num
                plag = 'B'
                total_turn += turn
            else:
                turn = num
                b_position = num
                plag = 'B'
                total_turn = turn
                
        elif arr[2*i] == 'O' and plag == 'O': # 일치
            o_position = num
            turn += abs(num - int(arr[2*(i-1)+1])) +1 
            total_turn += abs(num - int(arr[2*(i-1)+1])) +1 
        elif arr[2*i] == 'O' and plag != 'O':
            if num <= turn + 1:
                turn = 1
                o_position = num
                plag = 'O'
                total_turn += turn
            else:
                turn = num
                o_position = num
                plag = 'O'
                total_turn =turn
        #print(f'num: {num} , turn: {turn} , t : {total_turn} , plag : {plag}')

# idx 0 1 2 3 4 5 6 7
# arr b 2 o 1 o 2 b 4
# i   0   1   2   3
# B 5 O 8 #5turn # 3턴 더들어감  .8 - turn
# B 5 O 6 #5turn # 바로 버튼 누름 # o 위치 3 갱신
# B 5 O 3 #5turn # 바로 버튼 누름 # o의 위치는 3 갱신
    print(f'#{tc} {total_turn}')
# 3 B 5 B 8 O 100
# 4 B 2 O 1 O 2 B 4
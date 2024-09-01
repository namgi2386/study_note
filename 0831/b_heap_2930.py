import sys
sys.stdin = open('z2.txt' , 'r')


def insert_num(num):
    global pointer , word
                                                            # 우선 마지막노드에 삽입하기
    pointer += 1                                                # 빈칸으로 이동
    word[pointer] = num                                         # 삽입
    
                                                        # 숫자비교 더 크면 노드위치 스왑
    temp_p = pointer
    while temp_p > 1:                                           # 부모노드가 0이 아닐때
        if word[temp_p//2] < word[temp_p] :                       # 부모값이 더 작음
            word[temp_p] , word[temp_p//2] = word[temp_p//2] ,word[temp_p] # 스왑
            temp_p //= 2
        else:
            break                                                   # 아니면 끝냄
    return

def pop_max():
    global pointer , word

    if not pointer:                                                 # word에 값이 없음
        return -1

    maximum_result = word[1]                                        # 1번노드(루트) == 최댓값 저장
    word[1] = word[pointer]                                         # 마지막노드를 1번자리로 이동
    word[pointer] = 0
    pointer -= 1

    top = 1
    while top*2 <= pointer and word[top*2] :                   # 자식노드가 존재함
        compare_num_idx = top*2
        if top*2+1:                                            # 오른쪽 자식도 있을땐 자식간 크기비교
            if word[top*2+1] > word[top*2]:
                compare_num_idx = top*2+1
        
        if word[top] < word[compare_num_idx]:                       # 자식이 더클때,
            word[top] , word[compare_num_idx] = word[compare_num_idx] ,word[top] # 스왑
            top = compare_num_idx
        else:
            break                                                   # 아니면 끝냄
    
    return maximum_result



for tc in range(1,int(input())+1):
    n = int(input())

    word = [0]*(n+1)
    pointer = 0                                 # 마지막 노드의 위치 기록

    result_arr =[]
    for i in range(n):
        arr = list(map(int,input().split()))
        if len(arr) == 2:                       # 숫자(arr[1]) 추가
            insert_num(arr[1])
        else:                                   # 최댓값 출력
            result_arr.append(pop_max())
    
    print(f'#{tc}' , end =" ")
    print(*result_arr)

import sys
sys.stdin = open('z4.txt' ,'r')


def get_up(li):
    for i in range(10):
        if li[i] == 3:                      # 같은카드가 3장
            return True
    for i in range(8):
        if li[i] and li[i+1] and li[i+2] :  # 연속된 3장이 한장이상
            return True


for tc in range(1,int(input()) +1):
    arr = list(map(int,input().split()))    # 카드리스트
    odd_arr = [0]*10                        #  player 1 뽑은카드번호를 인덱스로하여 저장
    even_arr =[0]*10                        #  player 2  즉, 7을3번뽑으면, 7번인덱스에 3저장됨
    result = 0
    for i in range(12):                     # 12장 뽑을 예정
        num = arr[i]                        # 카드 하나씩 뽑기
        if not i%2:
                                            # odd_arr =   player 1 
            odd_arr[num] += 1               # 뽑은카드 기록하기
            if get_up(odd_arr):             # 검사하기
                result = 1                  # 통과하면 끝내기
                break
        else:
                                            # even_arr =   player 2
            even_arr[num] += 1
            if get_up(even_arr):
                result = 2
                break
    
    print(f'#{tc} {result}')
import sys
sys.stdin = open('z3piz.txt' , 'r' )

T= int(input())

def pizzang(n,m,arr):
    front = -1              # 현재   V
    rear = -1               # 현재   V 
                            #인덱스 -1  0  1  2  3  4  5 ...   
    q =[0]*1000             #         [0, 0, 0, 0, 0, 0, 0, 0,,,,,]

    # 우선 n개의 피자 넣고 시작
    # 큐의 형태는 # [  [피자번호 , 치즈의 양] , [피자번호 , 치즈의 양] , [피자번호 , 치즈의 양] .... ]
    for i in range(n):              
        q[i] = [i+1 , arr[i]]   # rear=2             v  
        rear +=1                # q = [[1,7],[2,2],[3,6],0,0,0,0,0,0,,,,,]

    p = n  # 현재 n개의 피자 넣었음
    while True :

        front +=1
        rear +=1

        if q[front][1] > 0:         # 피자 꺼내서 치즈 남았는지 확인하기
            q[rear]= [  q[front][0]  ,  q[front][1]//2  ]  # 치즈 절반으로 줄여서 다시 넣기
            if q[front][1]//2 == 0: #  절반으로 나눴는데 0이다? 새 피자 투입
                if p <m:
                    q[rear]=[p+1,arr[p]] # 새 피자 넣어주기 # p = n # n번째피자 넣어주기
                    p+=1                    # 넣어야할 피자 번호 체크

                else:               # 새피자 넣으려는데 남은 피자 없음

                    r = 0
                    for h in range(n):        # 현재피자부터 총 n개의 피자 
                        r += q[front+h][1]    # 화덕안에 남아있는 다른피자들의 치즈양 확인

                    if r==0 or r==1:
                        return q[rear][0]    #  다른피자들의 치즈양이 전부 0 일때의 피자번호 출력
                    
                    else:                       # 다른피자들이 아직 치즈남아있음
                        q[rear]=[q[front][0],0]  
        else:    # 에러방지코드
            q[rear]=[0,0]
        

for tc in range(1, T+1):
    n , m = map(int,input().split())       # n = 3 ,  m = 5
    arr = list(map(int,input().split()))  # [7, 2, 6, 5, 3]
    result = pizzang(n,m,arr)
    print(f'#{tc} {result}')


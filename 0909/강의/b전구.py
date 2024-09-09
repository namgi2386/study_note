import sys
sys.stdin = open('z2.txt' , 'r')
li =[]
for tc in range(1,int(input())+1):
    a ,b,c,d = map(int,input().split()) 
    start = max(a,c)
    end = min(b,d)

    result = end -start
    if result <= 0:
        result = 0
    
    # input/output 변환시간 
    # buffer에 저장출력하는시간의 문제
    li.append(result)

for i in range(len(li)):
    print(f'#{i+1} {li[i]}')
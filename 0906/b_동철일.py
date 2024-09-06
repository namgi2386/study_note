import sys
sys.stdin = open('z2.txt' , 'r')

def permutation(lev):
    if lev==n:
        print(stack)
        return
    
    for i in range(n):
        if i not in stack:
            stack.append(i)
            permutation(lev+1)
            stack.pop()

# stack=[]
# n=3
# permutation(lev =0)
'''
[0, 1, 2]
[0, 2, 1]
[1, 0, 2]
[1, 2, 0]
[2, 0, 1]
[2, 1, 0]
'''



def 동철fnc(lev , property): # lev=행 , property 계산할 확률
    global result

    # 종료조건
    if lev==n:
        result = max(result , property)
        return
    
    # 재귀호출
    for i in range(n):
        if i not in stack:
            stack.append(i)

            if property * arr[lev][i] > result:
                동철fnc( lev+1,   property * arr[lev][i]  )  
            
            stack.pop()


for tc in range(1,int(input())+1):
    n = int(input())

    # 입력값 미리 100으로 나눠주기
    arr=[list(map(lambda x: float(x)/100 ,input().split())) for _ in range(n)]
    
    '''       arr
    [0.71, 0.51, 0.30, 0.01]
    [0.29, 0.63, 0.32, 0.93]
    [0.84, 0.94, 0.33, 0.21]
    [0.56, 0.40, 0.80, 0.31]
    '''

    stack = []
    result = 0
    동철fnc(lev=0,property=1) # 레벨 , 확률

    result *=100

    print(f'#{tc} {result:.6f}')
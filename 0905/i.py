

def soon():
    if len(stack) == n:
        # my_arr = stack[:]
        yang(stack,0,0,0)
        return
    for i in range(n):
        if i not in stack:
            stack.append(i)
            soon()
            stack.pop()

def yang(my_arr , lev,left,right):
    global counts
    if lev==n:
        counts += 1
        return

    jey = maxium - left -right # 남은 추의 무게
    if jey+right <= left: # 오른쪽에 전부 놓아도 왼쪽보다 낮음
        counts += (1<<(n-lev)) # 점수 올려주고 리턴
        return

    #left에 넣기
    hey = arr[my_arr[lev]]
    yang(my_arr,lev+1,left+hey,right)

    if hey+right <= left: # 0 1 2 
        # right에 넣기
        yang(my_arr,lev+1,left,right+hey)
    
    




for tc in range(1,int(input()) +1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    maxium = sum(arr)
    counts = 0
    stack = []
    soon()

    print(f'#{tc} {counts}')


# left의 무게가 이미 남은 무게추의 합보다 클때 
# 즉 남은 무게추를 전부 right에 넣어도 left를 넘어서지 않을때
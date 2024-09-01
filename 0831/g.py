# def in_order(t):
#     global idx
#     global result
#     if t:
#         in_order(left[t])
#         if t ==1:
#             result[0] = idx
#         elif t==n//2:
#             result[1] = idx
#         idx +=1
#         in_order(right[t])

eng = ['a','b','c','d','e']

def in_order(t): # 인덱스가 들어감
    global word , num
    if t:
        in_order(left[t])
        word[t] = idx
        idx += 1

        in_order(right[t])






for tc in range(1,int(input())+1 ):

    n = int(input()) # n == 9
    left = [0]*(n+1)
    right = [0]*(n+1)
    word = [0]*(n+1)

    num = 1

    for i in range(2,n+1): # i == 2 ~ 9
        if left[i//2]==0:
            left[i//2] = i
        else:
            right[i//2] = i
    
    in_order(1)

    print(f'#{tc} {word[1]} {word[n//2]}')
    
    # idx = 1
    # result = [0,0]
    # print(f'#{tc} {result[0]} {result[1]}')
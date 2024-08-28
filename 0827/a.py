
def pre_order(t):
    global idx
    global result
    if t:
        pre_order(left[t])
        if t ==1:
            result[0] = idx
        elif t==n//2:
            result[1] = idx
        idx +=1
        pre_order(right[t])


for tc in range(1,int(input())+1 ):
    n = int(input())
    left = [0]*(n+1)   
    right = [0]*(n+1)
    for i in range(2,n+1):
        if left[i//2]==0:
            left[i//2] = i
        else:
            right[i//2] = i
    idx = 1
    result = [0,0]
    pre_order(1)
    print(f'#{tc} {result[0]} {result[1]}')




# 트리만든 뒤 값 채우기
# 트리만들면서 값 채우기

#idx 0 1 2 3 4 5 6 7 8 
#lef     1 2   3   6
#rig       4   7   8
# pre_order(n)



# left = [0]*(n+1)   
# right = [0]*(n+1)
# for i in range(2,n+1):
#     if left[i//2]==0:
#         left[i//2] = i
#     else:
#         right[i//2] = i

#idx 0 1 2 3 4 5 6 7 8 
#lef   2 4 6 8
#rig   3 5 7

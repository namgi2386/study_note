

def summer(arr):
    global anc
    if len(arr)==1:
        anc = int(arr[0])
        return
    
    result =0
    for i in range(len(arr)):
        result += int(arr[i])
    arr = list(str(result))
    summer(arr)


for tc in range(1,int(input())+1):
    arr = list(input())
    anc = 0
    summer(arr)
    print(f'#{tc} {anc}')
'''
3
5
108
588432'''


def summer(arr):
    
    result =0
    for i in range(len(arr)):
        result += int(arr[i])
        if result >= 10:
            result -= 9
    return result



for tc in range(1,int(input())+1):
    arr = list(input())
    anc = 0
    summer(arr)
    print(f'#{tc} {anc}')

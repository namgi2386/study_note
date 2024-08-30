import sys
sys.stdin = open('z1.txt' , 'r')

def hi():
    arr_set = set()
    for i in range(n):
        if int(arr[i],16):
            arr_set.add(arr[i])
    return list(arr_set)

def my(arr_total_soccer):
    result =[]
    for i in range(len(arr_total_soccer)):
        counts_1 =0
        counts_0 =0
        li =[]
        for j in range(len(arr_total_soccer[i])):
            if int(arr_total_soccer[i][j]):
                if counts_0:
                    li.append(counts_0)
                counts_1 += 1
                counts_0 = 0
            else:
                if counts_1:
                    li.append(counts_1)
                counts_1 = 0
                counts_0 += 1
        result.append(li)
    return result



for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    arr = [input()[:m] for _ in range(n)]

    arr_key = hi()
    n_key = len(arr_key)
    arr_antizer0 =[]

    for i in range(n_key):
        arr_antizer0.append(arr_key[i].strip('0'))
    
    arr_total_soccer =[]
    for i in range(len(arr_antizer0)):
        arr_total_soccer.append(bin(int(arr_antizer0[i],16))[2:])
    # print(my(arr_total_soccer))
    if tc == 1:
        print(my(['10101','1101']))

    # if tc == 15:
    #     print(len(arr_antizer0))


    # for i in range(n_key):
    #     x = bin(int(arr_key[i].strip('0'),16))[2:]
    #     arr_antizer0.append(x.strip('0'))

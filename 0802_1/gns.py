import sys
sys.stdin = open('z3.txt','r')

incording_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]


T = int(input())
for tc in range(1,T+1):
    str_num = input().split()
    n = int(str_num[1])
    text_list = list(input().split())
    zero_list = [0]*len(text_list)


    for x in range(len(incording_list)):
        for y in range(len(text_list)):
            if incording_list[x]==text_list[y]:
                zero_list[y] = x

    zero_list.sort()

    decording_list = [0]*len(zero_list)
    for num in range(10):
        for z in range(len(zero_list)):
            if num == zero_list[z]:
                decording_list[z] = incording_list[num]

    print(f'#{tc}')
    print(*decording_list)





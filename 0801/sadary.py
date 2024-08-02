import sys
sys.stdin = open('input.txt' , 'r')


for _ in range(10):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    num_2_index_j = 1000
    for idx in range(100):
        if arr[99][idx] == 2:
            num_2_index_j = idx

    pr = 99
    pc = num_2_index_j

    while pr !=0:
        if pc==0 and arr[pr][pc+1] == 0 :
            pr -= 1
        elif pc==0 and arr[pr][pc+1] == 1 :
            pc += 1

        if pc==99 and arr[pr][pc-1] ==0 :
            pr -= 1
        elif pc==99 and arr[pr][pc-1] ==1 :
            pc -= 1


        if 0< pc < 99 and arr[pr][pc+1] == 0 and arr[pr][pc-1] ==0 :
            pr -=1

        while 0< pc < 99 and arr[pr][pc+1] == 1 :
            pc += 1
            if pc == 99:
                pr -= 1
            elif pc < 99 and arr[pr][pc+1] == 0:
                pr -= 1
        while 0< pc < 99 and arr[pr][pc-1] == 1 :
            pc -= 1
            if pc== 0 :
                pr -= 1
            elif pc > 0 and arr[pr][pc - 1] == 0:
                pr -= 1

    print(tc , pr , pc)




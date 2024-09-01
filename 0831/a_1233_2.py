import sys
sys.stdin = open('z1.txt' , 'r')

operator = ['+','-','/','*']

for tc in range(1,11):
    n = int(input())
    result = 1
    for i in range(n):
        temp = list(map(lambda x :x if x in operator else int(x),input().split()))
        tn = len(temp)
        if tn in (1,3):
            result = 0
        if temp[0] in operator:
            result = 0
        if tn ==2 and temp[1] in operator:
            result = 0
        if tn == 4 and (temp[2] in operator or temp[3] in operator):
            result = 0

    print(f'{tc} {result}')
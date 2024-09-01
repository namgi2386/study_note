import sys
sys.stdin = open('z1.txt' , 'r')

operator = ['+','-','/','*']

def make_tree():
    global left , right , word
    temp = list(map(lambda x :x if x in operator else int(x),input().split()))
    
    word[temp[0]] = temp[1]
    if len(temp) >= 3:
        left[temp[0]] = temp[2]
        if temp[1] not in operator:
            return 0
        if len(temp) > 3:
            right[temp[0]] = temp[3]
        else:
            return 0
    return 1
    

for tc in range(1,11):
    n = int(input())
    left = [0]*(n+1)
    right = [0]*(n+1)
    word = [0]*(n+1)
    result = 1
    for i in range(n):
        if not make_tree():
            result = 0
    print(f'{tc} {result}')
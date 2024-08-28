dict = {}
lis_1 = [0]*10
lis_2 = [""]*10
lis_3 = ['a']*10

arr=['1','w','2','3']
dict[1]=arr[1]
lis_1[1] = arr[1]
lis_2[1] = arr[1]
lis_3[1] = arr[1]

print(dict)
print(lis_1)
print(lis_2)
print(lis_3)

import sys
sys.stdin = open('z2.txt' , 'r')

def inorder(t):
    if t:
        inorder(left[t])
        print(word[t] , end="")
        inorder(right[t])


for tc in range(1,11):
    n = int(input())
    word = [0]*101
    left =[0]*101
    right =[0]*101
    for i in range(n):
        arr = list(input().split())
        parent = int(arr[0])
        word[parent] = arr[1]
        if len(arr) >= 3:
            left[parent] = int(arr[2])
        if len(arr) == 4:
            right[parent] = int(arr[3])
    

    print(f'#{tc} ',end="")
    inorder(1)
    print()

import sys
sys.stdin = open('z1.txt','r')

for tc in range(1, int(input())+1):
    n,m = map(int ,input().split())
    arr = list(input())
    sep = n//4
    set_arr = arr[-sep:]
    set_arr.extend(arr)

    set_set =set()
    for i in range(4):
        for j in range(sep):
            set_set.add("".join(set_arr[i*sep+j:(i+1)*sep+j] ))
    arr = list(set_set)
    arrr=[]
    for i in range(len(arr)):
        arrr.append( int(arr[i],16) )
    arrr.sort(reverse=True)
    print(f'#{tc} {arrr[m-1]}')
'''
1
12 10
1B3B3B81F75E
'''
import sys
sys.stdin = open('z1.txt','r')

def boo():
    n , m , k = 78, 64, 4
    ar = '709 1087 1130 958 589 577 684 977 371 1116 1008 1221 373 1210 1151 544 1058 328 431 968 905 859 729 533 1161 225 568 652 751 1232 557 192 272 910 333 423 1291 815 250 795 956 1092 864 1064 1038 442 462 1324 188 350 615 451 315 272 220 1165 1179 684 141 740 795 213 275 96 477 968 861 1076 1249 890 493 253 462 117 126 1156 759 1356'
    arr = list(map(int, ar.split()))
    arr.append(0)
    boong_li = [0]*(12000*m)
    arr.sort()
    print(arr)
    
    #print(f'arr > {arr}')

    if arr[1] == 0:
        return 'Impossible'
    
    for i in range(1, n*m):
        boong_li[i] = (i//m)*k 
        
        if i in arr:
            if boong_li[i] < arr.index(i):
                print(f'{i} : {boong_li[i]} < {arr.index(i)}')
                return 'Impossible2'
    #print(f'bli > {boong_li}')
    print(f'#{373} : {boong_li[373]} < {arr.index(373)+1}')
    return 'Possible'

T = 1
for tc in range(1,T+1):
    result = boo()
    r = f'#998 {result}'
    print(r)
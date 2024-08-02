import sys
sys.stdin = open('z1.txt','r')

T = int(input())
for tc in range(1,T+1):
    str1 = list(input())
    str2 = list(input())

    key_list = list(set(str1))
    my_dict ={}
    for k in range(len(key_list)):
        my_dict[key_list[k]] = str2.count(key_list[k])
    max_v = 0
    for k,v in my_dict.items():
        if max_v < v:
            max_v = v
            result = k
    print(f'#{tc} {max_v}')


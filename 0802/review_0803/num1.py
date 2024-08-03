# import sys
# sys.stdin = open('input_bubble.txt','r')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    str1 = input()

    str2 = str1.split('0')

    str4 = " ".join(str2)
    max_str = 0
    print(str4)
    str3 = str4.split()
    for i in range(len(str3)):
        if max_str < len(str3[i]):
            max_str = len(str3[i])
    print(f'#{tc} {max_str}')

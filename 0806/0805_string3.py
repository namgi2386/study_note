t = int(input())
for tc in range(1,t+1):
    str1 = input()
    str2 = input()

    plen = len(str1)
    tlen = len(str2)

    pi = 0
    ti = 0

    result = 0

    while pi < plen and ti < tlen:
        if str1[pi] != str2[ti]:
            ti -= pi
            pi = -1
        ti += 1
        pi += 1

        if pi == plen:
            result = 1
            break
    print(f'#{tc} {result}')
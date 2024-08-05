T = 10
for tc in range(1,T+1):
    input()
    p = input() # 찾는 문자열 abcf
    t = input() # 전체 텍스트 abcdelajshdkjasd

    counts = 0

    pl = len(p)
    tl = len(t)

    pi = 0
    ti = 0

    while pi < pl and ti < tl :
        if t[ti] != p[pi]:
            ti -= pi                      # ti 1
            pi = -1                        # pi0
        ti += 1
        pi += 1

        if pi == pl :
            counts += 1

            ti = ti -pi +1
            pi = 0
    print(f'#{tc} {counts}')


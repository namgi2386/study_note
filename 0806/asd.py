T = int(input())
for tc in range(1, T+1):
    check = input() # akjsbdjb{{}}()((())))asdjg          ask        ()

    stack = []
    answer = 1
    top = -1
    hj = True

    for c in check:
        if c in '({':
            hj = False
            top +=1
            stack.append(c)
        if c == ')':
            if stack:
                if stack[top] == '(':
                    stack.pop()
                    top -= 1
                else:
                    answer = 0
                    break
            else:
                answer = 0
                break
        if c == '}':
            if stack:
                if stack[top] == '{':
                    stack.pop()
                    top -= 1
                else:
                    answer = 0
                    break
            else:
                answer = 0
                break
    else:
        if stack:
            answer = 0
        else:
            if hj:
                answer = 1
            else:
                answer = 0

    print(f'#{tc} {answer}')

T =int(input())
for tc in range(1,T+1):
    postfixed = input()
    stack =[]
    error_plag = False
    for token in postfixed:
        if token == '.':
            stack.append(token)
        if token not in '+-*/.':
            stack.append(int(token))

        else:
            right = stack.pop()
            left = stack.pop()

            if token == '+':
                result = left + right
            if token == '-':
                result = left - right
            if token == '*':
                result = left * right
            if token == '/':
                if right != 0:
                    result = int(left / right)
                else :
                    error_plag = True

            stack.append(result)

    if len(stack) == 2 :
        is_end = stack.pop()
        if is_end == '.':
            answer = stack.pop()
            print(f'#{tc} {answer}')
        else:
            print(f'#{tc} error')
    else:
        print(f'#{tc} error')
T = int(input())
for tc in range(1, T+1):
    check = input()

    stack = []
    answer = 1
    top = -1

    for c in check:
        if c == '(':
            top +=1
            stack.append(c)
        if c == ')':
            if stack:
                if stack[top] == '(':
                    stack.pop()
                    top -= 1
                else:
                    print(' 짝안맞음 : 중괄호 소괄호 안맞음')
                    answer = 0
                    break
            else:
                print('underflow : 배열에 아무것도 없는데 pop요청')
                answer = 0
                break
    else:
        if stack:
            print('남아있음 : 다끝났는데 stack에 뭔가 남아있음')
            answer = 0
    print(f'#{tc} {answer}')

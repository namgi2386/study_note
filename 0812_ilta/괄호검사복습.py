T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    n = len(arr)
    stack = []
    top = -1
    result = 1
    for i in range(n):
        if arr[i] in '({[':
            top +=1
            stack.append(arr[i])
        elif arr[i] in '}])':
            if stack:
                if arr[i] == ')' and stack[top] == '(':
                    stack.pop()
                    top -= 1
                elif arr[i] == '}' and stack[top] == '{':
                    stack.pop()
                    top -= 1
                elif arr[i] == ']' and stack[top] == '[':
                    stack.pop()
                    top -= 1
                else: 
                    result = -1
                    break
            else:
                result = -1
                break
        else:
            pass
    if stack:
        result = -1
    print(f'#{tc} {result}')

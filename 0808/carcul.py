import sys
sys.stdin = open('input.txt','r')

def get_postfix(infix,n):
    postfix =""
    stack =[]
    for i in range(n):
        if infix[i] != '+':
            postfix += infix[i]
        else:
            while stack:
                postfix += stack.pop()
            stack.append(infix[i])


    while stack:
        postfix += stack.pop()
    return postfix

def get_result(postfix):
    stack = []
    for token in postfix :
        if token != '+':
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            result = left + right
            stack.append(result)
    return stack.pop()


for tc in range(1,11):
    n = int(input())
    inpost = input()
    postfix = get_postfix(inpost,n)
    print(postfix)
    result = get_result(postfix)
    #print(f'#{tc} {result}')

import sys
sys.stdin = open('z1.txt','r')

def make_post(postfixed):
    stack =[]
    for token in postfixed:
        # if token == '.':
        #     stack.append(token)
        #     break
        if token.isdigit() :
            #print(token)
            stack.append(int(token))
        elif token == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'
        else:
            if len(stack) >=2:
                # if stack[-1] in '+-*/.':
                #     error_plag = True
                #     break 
                right = stack.pop()
                left = stack.pop()

                if token == '+':
                    result = left + right
                if token == '-':
                    result = left - right
                if token == '*':
                    result = left * right
                if token == '/':
                    result = left // right
                stack.append(result)
            else : return 'error' 


T =int(input())
for tc in range(1,T+1):
    postfixed = input().split()
    result = make_post(postfixed)
    print(f'#{tc} {result}')
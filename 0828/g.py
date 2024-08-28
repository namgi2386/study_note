import sys
sys.stdin = open('z3.txt' , 'r')

def post(t):
    global post_result
    if t:
        post(left[t])
        post(right[t])

        post_result.append(node[t])

def calcul():
    stack =[]
    for i in range(len(post_result)):
        x = post_result[i]
        if x not in '+-/*':
            stack.append(x)
        elif x == '+':
            r = int(stack.pop())
            l = int(stack.pop())
            stack.append(l+r)
        elif x == '-':
            r = int(stack.pop())
            l = int(stack.pop())
            stack.append(l-r)
        elif x == '*':
            r = int(stack.pop())
            l = int(stack.pop())
            stack.append(l*r)
        elif x == '/':
            r = int(stack.pop())
            l = int(stack.pop())
            stack.append(l//r)
    return stack.pop()

    

for tc in range(1,11):
    n = int(input())
    node = [""]*(n+1)
    left = [0]*(n+1)
    right = [0]*(n+1)
    post_result =[]

    for i in range(n):
        temp_arr = list(input().split())
        node[int(temp_arr[0])] = temp_arr[1]
        if len(temp_arr) == 4:
            left[int(temp_arr[0])] = int(temp_arr[2])
            right[int(temp_arr[0])] = int(temp_arr[3])
    post(1)
    print(f'#{tc} {calcul()}')


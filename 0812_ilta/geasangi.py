import sys
sys.stdin = open('z1.txt' , 'r')

dict_out = {'-':1,'+':1,'*':2,'/':2 ,'(':3}
dict_in = {'-':1,'+':1,'*':2,'/':2 ,'(':0}

def post_calculala(arr,n):
    result = ""
    stack = []
    top = -1
    for i in range(n):
        if arr[i] not in '+-*/()' :
            result += arr[i]
        elif arr[i] in '+-*/(':
            if not stack:
                top += 1
                stack.append(arr[i])
            else:    
                while top >= 0 and dict_in[stack[top]] >= dict_out[arr[i]]:
                    result += stack.pop()
                    top -= 1
                stack.append(arr[i])
                top += 1
        else: # ')'
            while stack[top] != '(':
                result += stack.pop()
                top -= 1
            result += stack.pop()
            top -= 1
    if stack:
        while top >=0:
            result += stack.pop()
            top -= 1
    return result
# #1 952*+1+33*7*6*9*1*7*+1+86*+61*1*5*2*4*7*+43*8*2*6*+78*4*5*+3+7+2+6+5+1+7+6+73*6*+2+6+62*+4+22*+49*3*+

def calcucu(post_arr , n):
    stack = []
    top = -1
    for i in range(n):
        if post_arr[i] not in '+-*/':
            top += 1
            stack.append(post_arr[i])
        elif post_arr[i] == '+':
            right = int(stack.pop())
            top -= 1
            left = int(stack.pop())
            top -= 1
            top += 1
            stack.append(left+right)
        elif post_arr[i] == '*':
            right = int(stack.pop())
            top -= 1
            left = int(stack.pop())
            top -= 1
            top += 1
            stack.append(left*right)

    return int(stack.pop())



T = 10
for tc in range(1,T+1):
    n = int(input())
    arr = list(input())
    
    post_result = post_calculala(arr,n)
    result = calcucu(post_result , n)
    print(f'#{tc} {result}')

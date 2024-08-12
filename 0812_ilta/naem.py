import sys
sys.stdin = open('z1.txt' , 'r')
# 중위표기식(infix) => 후위표기식(postfix)
# infix : 후위표기식으로 바꿀 중위표기식
# n : 식의 길이
 
icp = {"+":1, "*":2}
 
 
def get_postfix(infix, n):
    # 결과로 출력할 후위표기식
    postfix = ""
    stack = []
 
    for i in range(n):
        # infix[i] => 중위표기식의 i번째 글자
        if infix[i] not in "+*":
            # i번째 글자가 피연산자다 => 결과에 출력
            postfix += infix[i]
        else:
            while stack and icp[stack[-1]] >= icp[infix[i]]:
                postfix += stack.pop()
            stack.append(infix[i])
 
    while stack:
        postfix += stack.pop()
 
    return postfix
 
### 잘 되는지 확인하는 용도
# infix = "3+4+5*6+7"
# postfix = get_postfix(infix, len(infix))
 
# print(postfix)
 
 
 
# 후위표기식을 계산하는 함수
def get_result(postfix):
    stack = []
 
    # 후위표기식에서 글자 하나씩 떼어오기
    for token in postfix:
 
        # 떼어온 토큰이 피연산자이면 스택에 넣기
        if token not in "+*":
            stack.append(int(token))  # 타입 조심
        # 토큰이 연산자인 경우 연산에 필요한 만큼 스택에서 피연산자를 꺼낸 후 연산
        # 이 연산 결과를 다음 연산자가 또 써야 하기 때문에 다시 stack에 push
        else:
            # 오른쪽 피연산자가 먼저 나온다
            right = stack.pop()
            left = stack.pop()
            # 계산 결과
            result = 0
 
            # 연산자의 종류에 따라 계산
            if token == "+":
                result = left+right
            elif token == "*":
                result = left * right
 
            # 계산 결과를 다음 연산자가 써야하니까 스택에 다시 push
            stack.append(result)
 
    # 계산이 다 끝나면 스택 안에는 결과가 하나 남아있을 것이다
    return stack.pop()
 
T = 10
for tc in range(1, 11):
    L = int(input())
    infix = input()
 
    postfix = get_postfix(infix, L)
    result = get_result(postfix)
    # print(f'#{tc} {result}')
    print(f'#{tc} {postfix}')
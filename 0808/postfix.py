# 우선순위 표
# () > * / > + -
# 스택 밖에 있을 때 우선순위
icp = {"+":1, "-":1, "*":2, "/":2, "(":3 }
# 스택 안에 있을 때 우선순위
isp = {"+":1, "-":1, "*":2, "/":2, "(":0 }

# 중위표기식(infix) => 후위표기식(postfix)

# infix 후위 표기식으로 바꿀 중위표기식
# n 식의 길이

def get_postfix(infix,n):
    # 결과로 출력할 후위 표기식

    postfix =""

    stack =[]
    # 문자열에서 하나씩 떼어와서 식 만들자
    for i in range(n):
        # infix[i] => 중위표기식의 i번째 글짜
        if infix[i] not in "(+-*/)":
            # i번째 글자가 피연산자이다 => 결과로 바로출력
            postfix += infix[i]
        else:
            if infix[i] == ")": # 닫는괄호인지 검사
                # 여는괄호가 나올때까지 pop 해서 결과출력
                while stack:
                    # 하나꺼내기
                    op = stack.pop()
                    # 여는괄호면 꺼내기 중단
                    if op == "(":
                        break

                    # 여는괄호 아니면 출력
                    postfix += op
            else :
                # 현재 연산자(infix[i])의 우선순위(icp[infix[i]])보다
                # 스택의 top에 있는 연산자(stack[-1])의 우선순위(isp[stack[-1]])가 높다면
                # pop 해서 출력한다.
                # 예를들어 현재 '-' 인데 스택속에 '*,/' 있을때
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()

                # 스택의 탑에 있는 연산자의 우선순위가 나보다 작을땐,
                # push
                stack.append(infix[i])
    while stack:
        postfix += stack.pop()
    return postfix

infix = '(6+5*(2-8)/2)'
postfix = get_postfix(infix, len(infix))
print(postfix)

# 후위 표기식 계산함수
def get_result(postfix):
    stack = []

    # 후위표기식에서 글자 하나씩 떼어오기
    for token in postfix:

        # 때어온 토큰이 피연산자면 스택에 넣기
        if token not in "+-*/":
            stack.append(int(token))

        # 토큰이 연산자인 경우 연산에 필요한 만큼 스택에서
        # 피연산자를 꺼낸 후에 연산
        # 이 연산 결과를 다음 연산자가 또 써야 하기 때문에 다시 push
        else:
            right = stack.pop()
            left = stack.pop()

            result = 0
            # 연산자 종류에따라 계산
            if token == '+':
                result = left + right
            if token == '-':
                result = left - right
            if token == '*':
                result = left * right
            if token == '/':
                result = left / right

            # 계산결과를 다음 연산자가 써야하니까 스택에 다시 push
            stack.append(result)

    # 계산이 잘 되었다면 스택에는 하나의 값만 남아있을거임
    return stack.pop()

result = get_result(postfix)

print(result)
def push(item,size):
    global top
    top += 1
    if top == size:
        print('overflow')
    else:
        stack[top] = item

size = 10
stack = [0]*size
top = -1

push(10,size)
top += 1
stack[top] = 20

def my_pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top+1]
print(my_pop())

if top > -1 :
    top -= 1
    print(stack[top+1])


##############################
size = 10
stack = [0]*size
top = -1

#########   PUSH하기   #########

    #1 첫번째 추가 push(1)
top += 1
stack[top] = 1
    #2 두번째 추가 push(2)
top += 1
stack[top] = 2
    #3 세번째 추가 push(3)
top += 1
stack[top] = 3

#########   POP하기   #########

    #1 pop(1)
top -= 1
print(stack[top+1])
    #2 pop(2)
top -= 1
print(stack[top+1])
    #3 pop(3)
top -= 1
print(stack[top+1])
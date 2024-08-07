# T = int(input())
# for tc in range(1,T+1):
#     my_text , my_word = input().split()
#     word_idx = 0
#     text_idx = 0
#     result = 0
#     while word_idx < len(my_word) and  text_idx < len(my_text):
#
#         if my_word[word_idx] != my_text[text_idx] :
#             text_idx -= word_idx
#             word_idx = -1
#         text_idx += 1
#         word_idx += 1
#         if word_idx == len(my_word):
#             result += 1
#             text_idx = text_idx - word_idx +1
#             word_idx = 0
#     qq = len(my_text) - (len(my_word)-1)*result
#
#     print(f'#{tc} info :  {len(my_text)} {len(my_word)} {result}')
#     print(f'#{tc} {qq}')

T = int(input())
for tc in range(1,T+1):
    my_text , my_word = input().split()
    stack = []
    stack_str =""
    lt = len(my_text)
    lw = len(my_word)
    ls = len(stack)
    print(lt , lw , ls , my_word)

    for i in range(lt):
        stack.append(my_text[i])
        stack_str += my_text[i]
        if ls >= lw:
            print(stack[ls-1,ls-lw,-1])
            if stack_str[ls-1,ls-lw,-1] == my_word:
                print(f'{list[my_word]} ')
    # print()
    # print(stack)
    # print(list[my_word])
    # print()
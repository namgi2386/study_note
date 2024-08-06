import sys
sys.stdin = open('in.txt','r')

T = int(input())
for tc in range(1,T+1):
    my_text , my_word = input().split()
    word_idx = 0
    text_idx = 0
    result = 0
    while word_idx < len(my_word) and  text_idx < len(my_text):
        if my_word[word_idx] != my_text[text_idx] :
            text_idx -= word_idx
            word_idx = -1
        text_idx += 1
        word_idx += 1
        if word_idx == len(my_word):
            result += 1
            text_idx = text_idx - word_idx +1
            word_idx = 0

    #print(f'#{tc} info :  {len(my_text)} {len(my_word)} {result}')
    print(f'#{tc} {len(my_text) - len(my_word)*result + result }')

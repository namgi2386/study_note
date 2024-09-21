import sys
sys.stdin =open('z1.txt','r')



li = []
T=int(input())
for _ in range(T):
    arr = input()
    result =0
    for i in arr:
        result += int(i)
        if result >= 10:
            result -= 9
    li.append(result)
for tc in range(T):
    print(f'#{tc+1} {li[tc]}')

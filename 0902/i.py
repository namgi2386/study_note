import sys
sys.stdin = open('z2.txt' , 'r')

def f():
    if len(s) == n-1:
        total_arr.append(s[:]) # s[:]가 아닌 그냥 s 를 append하게되면 빈리스트가 들어감
        return
    for i in range(1,n):
        if i not in s:
            s.append(i)
            f()
            s.pop()


n = 4
s= []
total_arr = []
f()
print(total_arr)

# 출력값
'''
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
'''

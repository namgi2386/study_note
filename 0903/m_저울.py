def soon():
    if len(s) == 3:
        total_arr.append(s[:])
        return
    for i in range(n):
        if i not in s:
            s.append(i)
            soon()
            s.pop()


for tc in range(1,int(input()) +1):
    n = int(input())
    arr = list(map(int, input().split()))
    s = []
    total_arr =[]
    print(total_arr)
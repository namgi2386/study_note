def get_shortcut():
    global s
    nn = 5
    if len(s) == n-1:
        print(s)
        return

    for i in range(nn): # 0 1 2 3 4 
        if i not in s:
            s.append(i)
            get_shortcut()
            s.pop()

n = 4 
s = []
get_shortcut()

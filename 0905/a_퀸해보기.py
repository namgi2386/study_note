
def queen(step):
    if step==n:
        return
    
    for i in range(n):
        if not arr[step][i]:
            queen(step+1)


n=8
arr = [[0]*n for _ in range(n)]
queen(0)
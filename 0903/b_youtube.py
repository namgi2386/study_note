mem = ['a','b','c','d','e']

def bib(t):
    cnt =0
    checj_arr =[]
    for i in range(n):
        if t & (1<<i):
            cnt += 1
            checj_arr.append(mem[i])
    total_arr.append(checj_arr[:])
    return cnt

n =5
result = 0
total_arr = []
for rr in range(1<<n):
    
    if bib(rr) >= 2:
        result += 1
        print(total_arr)
    print(result)
lst = [1,2,3,4,5]
N = 5

def make_perm(idx , selected , result , n):

    if idx == n:
        print(result)
        return

    for i in range(n):
        if selected[i] == 0: 
            selected[i] = 1
            result.append(lst[i])
            make_perm(idx+1 , selected , result , n )
            selected[i] = 0
            result.pop()
make_perm(0,[0]*N , [] , N)

tc = 200000
i = 0
j = 1
k = 1
li=[1,1,1,1,1,1,0,1,1,1,1,1]
while tc != 0:
    mark = '-'
    position = '|'
    print(f'{mark*(5-k)} @ {mark*k}  {mark*10}{position*li[i]}{mark*(10-3*li[i])}')
    i = (i+1)%11
    j = 6 - i
    k = abs(j)
    tc -= 1
